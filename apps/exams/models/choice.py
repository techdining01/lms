from django.db import models


class Choice(models.Model):
    question = models.ForeignKey(
        "exams.Question",
        on_delete=models.CASCADE,
        related_name="choices",
    )

    text = models.CharField(max_length=500)

    is_correct = models.BooleanField(default=False)
