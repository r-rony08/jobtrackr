from django.urls import path
from .views import test_auth_app, protected_test, register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView, recruiter_test


urlpatterns = [
    path('test/', test_auth_app, name='test_auth_app'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', protected_test, name='protected_test'),
    path('register/', register_user, name='register_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('recruiter-test/', recruiter_test),


]