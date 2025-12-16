from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

def test_auth_app(request):
    return JsonResponse({'status': 'auth_app is working'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_test(request):
    return Response({'status': 'JWT authentication works', 'user': request.user.email})
