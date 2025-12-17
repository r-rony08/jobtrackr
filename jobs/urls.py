from django.urls import path
from .views import create_job, list_jobs

urlpatterns = [
    path('', list_jobs),
    path('create/', create_job),
]
