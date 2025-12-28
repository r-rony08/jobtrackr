from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from .serializers import ApplicationSerializer, ApplicationStatusUpdateSerializer
from jobs.models import Job
from auth_app.permissions import IsUser
from auth_app.permissions import IsRecruiter
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from django.db.models import Count


class ApplyJobView(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsUser]

    @extend_schema(
        request=ApplicationSerializer,
        responses={201: ApplicationSerializer}
    )
    def perform_create(self, serializer):
        job = get_object_or_404(Job, id=self.kwargs['job_id'], is_active=True)

        if Application.objects.filter(job=job, user=self.request.user).exists():
            raise ValueError("Already applied")

        serializer.save(
            user=self.request.user,
            job=job
        )


# View Applications (Recruiter Only)

class RecruiterApplicationsView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        job = get_object_or_404(
            Job,
            id=self.kwargs['job_id'],
            recruiter=self.request.user
        )
        return job.applications.select_related('user')



class UpdateApplicationStatusView(UpdateAPIView):
    serializer_class = ApplicationStatusUpdateSerializer  
    permission_classes = [IsAuthenticated, IsRecruiter]
    queryset = Application.objects.all()
    http_method_names = ['patch']


class UserApplicationAnalyticsView(APIView):
    permission_classes = [IsAuthenticated, IsUser]

    def get(self, request):
        total = Application.objects.filter(user=request.user).count()

        status_breakdown = (
            Application.objects
            .filter(user=request.user)
            .values('status')
            .annotate(total=Count('id'))
        )

        return Response({
            "total_applications": total,
            "status_breakdown": status_breakdown
        })



class RecruiterApplicationAnalyticsView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        data = (
            Application.objects
            .filter(job__recruiter=request.user)
            .values('status')
            .annotate(total=Count('id'))
        )

        return Response({
            "applications_by_status": data
        })