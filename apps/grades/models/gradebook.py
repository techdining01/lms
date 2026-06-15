from django.db import models


class Gradebook(models.Model):
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

    ca_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    exam_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    total_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    grade = models.CharField(max_length=5)

    remark = models.CharField(max_length=100)
