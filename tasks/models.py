from django.db import models
from django.conf import settings

class Task(models.Model):
    SH = "School"
    WK = "Work"
    HS = "Home"
    OTH = "Other"
    TASK_TYPE_CHOICES = [
        (SH, "School"),
        (WK, "Work"),
        (HS, "Home"),
        (OTH, "Other"),
    ]
    task_type = models.CharField(max_length=6, choices=TASK_TYPE_CHOICES, default=OTH)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (by {self.owner})"