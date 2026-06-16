from django.db import models


class Exam(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        CLOSED = "CLOSED", "Closed"

    title = models.CharField(max_length=255)

    instructions = models.TextField()

    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        "learning.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.CASCADE,
    )

    duration_minutes = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField(default=100)

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    allow_resume = models.BooleanField(default=True)

    shuffle_questions = models.BooleanField(default=True)

    shuffle_options = models.BooleanField(default=True)

    max_attempts = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
