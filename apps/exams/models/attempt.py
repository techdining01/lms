from django.db import models


class ExamAttempt(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS"

        SUBMITTED = "SUBMITTED"

        AUTO_SUBMITTED = "AUTO_SUBMITTED"

    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
    )

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    started_at = models.DateTimeField(auto_now_add=True)

    submitted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.IN_PROGRESS,
    )

    tab_switch_count = models.PositiveIntegerField(default=0)
