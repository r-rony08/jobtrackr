from django.urls import path
from .views import apply_job, recruiter_applications

urlpatterns = [
    path('apply/<int:job_id>/', apply_job),
    path('job/<int:job_id>/applications/', recruiter_applications),
]
