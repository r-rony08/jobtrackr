from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Job
from .serializers import JobSerializer
from .permissions import IsJobOwner
from auth_app.permissions import IsRecruiter


# Create Job Recruiter Only

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsRecruiter])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.save(recruiter=request.user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# List Jobs

@api_view(['GET'])
@permission_classes([AllowAny])
def list_jobs(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


# Update Jobs

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsRecruiter, IsJobOwner])
def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    serializer = JobSerializer(
        job,
        data=request.data,
        partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

# Delete Jobs

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsRecruiter, IsJobOwner])
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.is_active = False
    job.save()

    return Response(
        {"message": "Job deactivated"},
        status=status.HTTP_204_NO_CONTENT
    )
