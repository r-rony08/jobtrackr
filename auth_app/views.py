from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.decorators import throttle_classes
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, MyTokenObtainPairSerializer
from .permissions import IsRecruiter
from core.utils.api_response import api_response
from .throttles import AuthThrottle, LoginThrottle
from profiles.models import UserProfile
from drf_spectacular.utils import extend_schema

# Create your views here.

class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "user": {"type": "string"}
                        }
                    },
                    "message": {"type": "string"}
                }
            }
        }
    )
    def get(self, request):
        return api_response(
            success=True,
            data={"user": request.user.email},
            message="JWT authentication works",
            status=status.HTTP_200_OK
        )


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AuthThrottle]  

    @extend_schema(
        request=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer}
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # auto-create profile
            UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    "full_name": f"{user.first_name} {user.last_name}",
                    "phone": "",
                    "location": "",
                    "bio": ""
                }
            )

            return Response({
                "success": True,
                "data": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role
                },
                "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "data": serializer.errors,
            "message": "Validation error"
        }, status=status.HTTP_400_BAD_REQUEST)



# Create Custom Login View

class MyTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [LoginThrottle]
    serializer_class = MyTokenObtainPairSerializer


class RecruiterTestView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    @extend_schema(
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "data": {"type": "null"},
                    "message": {"type": "string"}
                }
            }
        }
    )
    def get(self, request):
        return api_response(
            success=True,
            data=None,
            message="Recruiter access granted",
            status=status.HTTP_200_OK
        )

