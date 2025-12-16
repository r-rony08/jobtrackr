from django.urls import path
from .views import test_auth_app

urlpatterns = [
    path('test/', test_auth_app, name='test_auth_app'),
]