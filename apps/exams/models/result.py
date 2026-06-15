from django.db import models


class ExamResult(models.Model):
    attempt = models.OneToOneField(
        "exams.ExamAttempt",
        on_delete=models.CASCADE,
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    grade = models.CharField(max_length=10)

    remarks = models.TextField(blank=True)
