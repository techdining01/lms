from django.conf import settings
from django.db import models


class Assignment(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        CLOSED = "CLOSED", "Closed"

    title = models.CharField(max_length=255)

    instructions = models.TextField()

    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
        related_name="assignments",
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        "learning.Course",
        on_delete=models.CASCADE,
        related_name="assignments",
        null=True,
        blank=True,
    )

    due_date = models.DateTimeField()

    total_marks = models.PositiveIntegerField(default=100)

    late_penalty_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    allow_text_submission = models.BooleanField(default=True)

    allow_file_submission = models.BooleanField(default=True)

    max_attempts = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_assignments",
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title
