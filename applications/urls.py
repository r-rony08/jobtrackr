from django.urls import path
from .views import ApplyJobView, RecruiterApplicationsView, UpdateApplicationStatusView, UserApplicationAnalyticsView, RecruiterApplicationAnalyticsView 

urlpatterns = [
    path('apply/<int:job_id>/', ApplyJobView.as_view()),
    path('job/<int:job_id>/applications/', RecruiterApplicationsView.as_view()),
    path('application/<int:pk>/status/', UpdateApplicationStatusView.as_view()),
    path('analytics/user/', UserApplicationAnalyticsView.as_view()),
    path('analytics/recruiter/', RecruiterApplicationAnalyticsView.as_view()),
]
