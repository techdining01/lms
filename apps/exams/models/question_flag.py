from django.db import models


class QuestionFlag(models.Model):
    attempt = models.ForeignKey(
        "exams.ExamAttempt",
        on_delete=models.CASCADE,
    )

    question = models.ForeignKey(
        "exams.QuestionBank",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
