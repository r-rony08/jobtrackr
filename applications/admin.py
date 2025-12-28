from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'job',
        'status',
        'applied_at',
    )

    list_filter = ('status', 'applied_at')
    search_fields = ('user__email', 'job__title')
    ordering = ('-applied_at',)

    readonly_fields = ('applied_at',)
