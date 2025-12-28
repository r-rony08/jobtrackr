from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application
        fields = [
            'id',
            'job',
            'job_title',
            'user_email',
            'cover_letter',
            'status',
            'applied_at'
        ]
        read_only_fields = [
            'status',
            'applied_at'
        ]

class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["status"]

    def validate_status(self, value):
        allowed = ["applied", "interview", "offer", "rejected"]
        if value not in allowed:
            raise serializers.ValidationError("Invalid status")
        return value
