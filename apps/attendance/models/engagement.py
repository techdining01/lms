from django.db import models


class StudentEngagement(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    lesson = models.ForeignKey(
        "course_delivery.Lesson",
        on_delete=models.CASCADE,
    )

    minutes_spent = models.PositiveIntegerField(default=0)

    last_accessed = models.DateTimeField(auto_now=True)
