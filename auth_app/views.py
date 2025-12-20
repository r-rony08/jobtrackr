from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from .permissions import IsRecruiter
from core.utils.api_response import api_response
from rest_framework.decorators import throttle_classes
from .throttles import AuthThrottle, LoginThrottle


# Create your views here.

def test_auth_app(request):
    return JsonResponse({'status': 'auth_app is working'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_test(request):
    return api_response(
    success=True,
    data={
        "user": request.user.email
    },
    message="JWT authentication works",
    status=status.HTTP_200_OK
)


@api_view(['POST'])
@throttle_classes([AuthThrottle])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return api_response(
    success=True,
    data={
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    },
    message="User registered successfully",
    status=status.HTTP_201_CREATED
)
    return api_response(
    success=False,
    data=serializer.errors,
    message="Validation error",
    status=status.HTTP_400_BAD_REQUEST
)


# Create Custom Login View

class MyTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [LoginThrottle]
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsRecruiter])
def recruiter_test(request):
    return api_response(
    success=True,
    data=None,
    message="Recruiter access granted",
    status=status.HTTP_200_OK
)

