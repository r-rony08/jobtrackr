from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.response import Response

class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: UserProfileSerializer}
    )
    def get(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile)
        return Response({
            "success": True,
            "data": serializer.data,
            "message": "Profile retrieved successfully"
        })

    @extend_schema(
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def patch(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": True,
            "data": serializer.data,
            "message": "Profile updated successfully"
        })
