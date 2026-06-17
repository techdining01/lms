from django.db import models


class NotificationTemplate(models.Model):
    key = models.CharField(
        max_length=100,
        unique=True,
    )

    subject = models.CharField(max_length=255)

    body = models.TextField()

    is_active = models.BooleanField(default=True)
