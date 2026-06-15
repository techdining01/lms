from django.contrib.auth import models


class Announcement(models.Model):
    title = models.CharField(max_length=255)

    content = models.TextField()

    audience = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)


