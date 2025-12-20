from django.db import models
from django.conf import settings

# Create your models here.

class Job(models.Model):

    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    INTERN = 'intern'

    JOB_TYPE_CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (INTERN, 'Intern'),
    )

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()

    location = models.CharField(max_length=255, db_index=True)
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        db_index=True
    )

    salary = models.PositiveIntegerField(
        null=True, blank=True
    )

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

