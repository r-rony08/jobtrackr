from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'recruiter',
        'job_type',
        'location',
        'salary',
        'is_active',
        'created_at',
    )

    list_filter = ('job_type', 'is_active', 'location')
    search_fields = ('title', 'recruiter__email', 'location')
    ordering = ('-created_at',)

    readonly_fields = ('created_at',)
