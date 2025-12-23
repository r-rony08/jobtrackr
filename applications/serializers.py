from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application
        fields = ('id', 'job', 'job_title', 'user', 'user_email', 'cover_letter', 'status', 'applied_at')
        read_only_fields = ('user', 'status', 'applied_at')
   
            
   

