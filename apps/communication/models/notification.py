from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=255)

    message = models.TextField()

    publish_at = models.DateTimeField()

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
    )
