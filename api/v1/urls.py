from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth_app.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
    path('profiles/', include('profiles.urls')),
]