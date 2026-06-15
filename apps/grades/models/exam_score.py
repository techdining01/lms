from django.db import models


class ExamScore(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
    )

    score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
