from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from core.utils.api_response import api_response   
from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    cache.clear()


    return Response(serializer.data, status=status.HTTP_201_CREATED)


# List Jobs

@api_view(['GET'])
@permission_classes([AllowAny])
def list_jobs(request):
    cache_key = "jobs:list"
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    jobs = (
        Job.objects
        .select_related('recruiter')
        .filter(is_active=True)
        .order_by('-created_at')
    )

    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(jobs, request)

    serializer = JobSerializer(result_page, many=True)
    cache.set(cache_key, serializer.data, timeout=300)
    return api_response(
        success=True,
        data={
            "count": paginator.page.paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": serializer.data
        },
        message="Jobs retrieved successfully",
        status=200
    )



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
    cache.clear()


    return api_response(
    success=True,
    data=serializer.data,
    message="Job updated successfully",
    status=status.HTTP_200_OK
)


# Delete Jobs

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsRecruiter, IsJobOwner])
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.is_active = False
    job.save()
    cache.clear()


    return Response(status=status.HTTP_204_NO_CONTENT)


## Search & Filter Jobs

@api_view(['GET'])
@permission_classes([AllowAny])
def search_jobs(request):
    query_string = request.META.get("QUERY_STRING", "")
    cache_key = f"jobs:search:{query_string}"

    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    jobs = Job.objects.select_related('recruiter')

    is_active = request.GET.get('is_active', 'true').lower() == 'true'
    jobs = jobs.filter(is_active=is_active)

    title = request.GET.get('title')
    if title:
        jobs = jobs.filter(title__icontains=title)

    location = request.GET.get('location')
    if location:
        jobs = jobs.filter(location__icontains=location)

    serializer = JobSerializer(jobs, many=True)
    cache.set(cache_key, serializer.data, 300)

    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(jobs, request)

    serializer = JobSerializer(result_page, many=True)

    return api_response(
        success=True,
        data={
            "count": paginator.page.paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": serializer.data
        },
        message="Jobs retrieved successfully",
        status=200
    )
