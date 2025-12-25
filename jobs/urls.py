from django.urls import path
from .views import CreateJobView, ListJobsView, UpdateJobView, DeleteJobView, SearchJobsView

urlpatterns = [
    path('', ListJobsView.as_view()),
    path('create/', CreateJobView.as_view()),
    path('<int:pk>/update/', UpdateJobView.as_view()),
    path('<int:pk>/delete/', DeleteJobView.as_view()),
    path('search/', SearchJobsView.as_view()),
]
