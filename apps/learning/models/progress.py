from django.db import models


class LessonProgress(models.Model):
    learner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    lesson = models.ForeignKey("learning.Lesson", on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    completed_at = models.DateTimeField(null=True, blank=True)
