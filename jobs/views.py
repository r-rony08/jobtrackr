from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Job
from .serializers import JobSerializer
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


