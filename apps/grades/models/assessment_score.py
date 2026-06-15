from django.db import models


class AssessmentScore(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.CASCADE,
    )

    assignment_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    attendance_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )
