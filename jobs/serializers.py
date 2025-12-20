from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    recruiter_email = serializers.EmailField(
        source='recruiter.email',
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'location',
            'job_type',
            'salary',
            'recruiter_email',
            'created_at'
        ]

