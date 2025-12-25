from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, ProtectedTestView, RecruiterTestView,RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedTestView.as_view(), name='protected_test'),
    path('recruiter-test/', RecruiterTestView.as_view(), name='recruiter_test'),
]