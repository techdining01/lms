from django.db import models


class Exam(models.Model):
    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=255)

    duration_minutes = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
