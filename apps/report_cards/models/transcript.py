from django.db import models


class Transcript(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    generated_at = models.DateTimeField(auto_now_add=True)
