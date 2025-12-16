from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test_auth_app(request):
    return JsonResponse({'status': 'auth_app is working'})