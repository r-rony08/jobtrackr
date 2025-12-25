from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema
from .models import Job
from .serializers import JobSerializer
from auth_app.permissions import IsRecruiter
from django.core.cache import cache
from .permissions import IsJobOwner
from core.pagination import StandardPagination

# Create Jobs
class CreateJobView(CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    @extend_schema(
        request=JobSerializer,
        responses={201: JobSerializer}
    )
    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)
        cache.clear()
 


# List Jobs

class ListJobsView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardPagination

    def get_queryset(self):
        return (
            Job.objects
            .select_related('recruiter')
            .filter(is_active=True)
            .order_by('-created_at')
        )



# Update Jobs
class UpdateJobView(RetrieveUpdateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter, IsJobOwner]
    queryset = Job.objects.all()

    def perform_update(self, serializer):
        serializer.save()
        cache.clear()


# Delete Jobs
class DeleteJobView(DestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter, IsJobOwner]
    queryset = Job.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        cache.clear()


## Search & Filter Jobs

class SearchJobsView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardPagination

    def get_queryset(self):
        qs = Job.objects.select_related('recruiter').filter(is_active=True)

        title = self.request.GET.get('title')
        location = self.request.GET.get('location')
        job_type = self.request.GET.get('job_type')

        if title:
            qs = qs.filter(title__icontains=title)
        if location:
            qs = qs.filter(location__icontains=location)
        if job_type:
            qs = qs.filter(job_type=job_type)

        return qs.order_by('-created_at')
