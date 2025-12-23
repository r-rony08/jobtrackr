from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from applications.models import Application
from .serializers import ApplicationSerializer
from jobs.models import Job
from django.db.models import Count

# Apply to Job Users Only

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request, job_id):
    if request.user.role != 'user':
        return Response({"detail": "Only users can apply"}, status=status.HTTP_403_FORBIDDEN)

    job = get_object_or_404(Job, id=job_id, is_active=True)

    # Prevent duplicate
    if Application.objects.filter(job=job, user=request.user).exists():
        return Response({"detail": "Already applied"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ApplicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user, job=job)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

# View Applications (Recruiter Only)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recruiter_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)
    applications = job.applications.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count

from applications.models import Application
from jobs.models import Job


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def application_analytics(request):
    user = request.user

    # ---------- PATCH → Update application status ----------
    if request.method == 'PATCH':
        application_id = request.data.get('application_id')
        new_status = request.data.get('status')

        if not application_id or not new_status:
            return Response(
                {"success": False, "message": "application_id and status are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        application = get_object_or_404(
            Application,
            id=application_id,
            user=user
        )

        if new_status not in dict(Application.STATUS_CHOICES):
            return Response(
                {"success": False, "message": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        application.status = new_status
        application.save()

        return Response({
            "success": True,
            "message": "Application status updated"
        })

    # ---------- GET → Analytics ----------
    # Total jobs (for recruiter)
    total_jobs = Job.objects.filter(recruiter=user).count() if getattr(user, 'role', None) == 'recruiter' else 0

    # Total applications by user
    total_applications = Application.objects.filter(user=user).count()

    # Status-wise count
    status_counts_qs = (
        Application.objects
        .filter(user=user)
        .values('status')
        .annotate(count=Count('id'))
    )
    status_counts = [{"status": item["status"], "total": item["count"]} for item in status_counts_qs]

    # Jobs by company
    jobs_by_company_qs = (
        Application.objects
        .filter(user=user)
        .values('job__title')
        .annotate(count=Count('id'))
    )
    jobs_by_company = [{"job__title": item["job__title"], "total": item["count"]} for item in jobs_by_company_qs]

    # Recent applications
    recent_applications_qs = (
        Application.objects
        .filter(user=user)
        .select_related('job')
        .order_by('-applied_at')[:5]
    )
    recent_data = [
        {
            "job_title": app.job.title,
            "status": app.status,
            "applied_at": app.applied_at
        }
        for app in recent_applications_qs
    ]

    return Response({
        "success": True,
        "data": {
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "status_breakdown": status_counts,
            "jobs_by_company": jobs_by_company,
            "recent_applications": recent_data
        },
        "message": "Analytics retrieved successfully"
    })
