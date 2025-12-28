from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'phone',
        'location',
        'created_at',
    )

    search_fields = ('full_name', 'user__email', 'phone')
    list_filter = ('created_at',)
