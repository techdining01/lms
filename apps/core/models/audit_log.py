from django.db import models


class AuditLog(models.Model):
    actor = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    action = models.CharField(max_length=255)

    object_id = models.CharField(max_length=100)

    content_type = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
