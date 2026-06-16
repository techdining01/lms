from django.db import models


class ExamResult(models.Model):
    position = models.PositiveIntegerField(default=0)
    
    attempt = models.OneToOneField(
        "exams.ExamAttempt",
        on_delete=models.CASCADE,
    )

    objective_score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    subjective_score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    total_score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    percentage = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )





