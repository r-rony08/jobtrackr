from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    recruiter_email = serializers.ReadOnlyField(
        source='recruiter.email'
    )

    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'description',
            'location',
            'job_type',
            'salary',
            'is_active',
            'created_at',
            'recruiter_email',
        )
