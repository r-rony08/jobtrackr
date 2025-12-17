# every user always has a profile without relying on API calls.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile

User = settings.AUTH_USER_MODEL      # keeps the model flexible and compatible with custom user models.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, full_name="")
