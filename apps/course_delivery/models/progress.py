from django.db import models


class LessonProgress(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED"
        IN_PROGRESS = "IN_PROGRESS"
        COMPLETED = "COMPLETED"

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="lesson_progress",
        limit_choices_to={"role": "STUDENT"},
    )

    lesson = models.ForeignKey(
        "course_delivery.Lesson",
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = (
            "student",
            "lesson",
        )
