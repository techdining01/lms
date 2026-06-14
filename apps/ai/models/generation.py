from django.db import models


class AIGeneration(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    prompt = models.TextField()

    response = models.TextField()

    feature = models.CharField(max_length=100)

    tokens_used = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
