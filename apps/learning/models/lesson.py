from django.db import models


class Lesson(models.Model):
    class LessonType(models.TextChoices):
        VIDEO = "VIDEO", "Video"
        ARTICLE = "ARTICLE", "Article"
        QUIZ = "QUIZ", "Quiz"
        ASSIGNMENT = "ASSIGNMENT", "Assignment"

    section = models.ForeignKey(
        "learning.Section", on_delete=models.CASCADE, related_name="lessons"
    )

    title = models.CharField(max_length=255)

    lesson_type = models.CharField(max_length=20, choices=LessonType.choices)

    content = models.TextField(blank=True)

    video_url = models.URLField(blank=True)

    duration_seconds = models.PositiveIntegerField(default=0)

    order = models.PositiveIntegerField()

    is_preview = models.BooleanField(default=False)
