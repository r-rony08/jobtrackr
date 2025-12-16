from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
# Create your views here.

def test_auth_app(request):
    return JsonResponse({'status': 'auth_app is working'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_test(request):
    return Response({'status': 'JWT authentication works', 'user': request.user.email})

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message": "User registered successfully",
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)