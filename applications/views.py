from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Application
from .serializers import ApplicationSerializer
from jobs.models import Job

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
