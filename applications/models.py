from django.db import models
from django.conf import settings
from jobs.models import Job

User = settings.AUTH_USER_MODEL


class Application(models.Model):

    APPLIED = 'applied'
    INTERVIEW = 'interview'
    REJECTED = 'rejected'
    OFFER = 'offer'

    STATUS_CHOICES = (
        (APPLIED, 'Applied'),
        (INTERVIEW, 'Interview'),
        (REJECTED, 'Rejected'),
        (OFFER, 'Offer'),
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    cover_letter = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=APPLIED,
        db_index=True
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'user')

    def __str__(self):
        return f"{self.user.email} → {self.job.title} ({self.status})"
