
from django.db import models


class ExamAttempt(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
    )

    started_at = models.DateTimeField(auto_now_add=True)

    submitted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )