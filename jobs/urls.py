from django.urls import path
from .views import create_job, list_jobs,update_job, delete_job

urlpatterns = [
    path('', list_jobs),
    path('create/', create_job),
    path('<int:job_id>/update/', update_job),
    path('<int:job_id>/delete/', delete_job),
]