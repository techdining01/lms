
from django.db import models


class UserNotificationPreference(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    email_notifications = models.BooleanField(default=True)

    sms_notifications = models.BooleanField(default=True)

    push_notifications = models.BooleanField(default=True)
