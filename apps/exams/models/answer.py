from django.db import models


class Answer(models.Model):
    attempt = models.ForeignKey(
        "exams.ExamAttempt",
        on_delete=models.CASCADE,
        related_name="answers",
    )

    question = models.ForeignKey(
        "exams.Question",
        on_delete=models.CASCADE,
    )

    selected_option = models.ForeignKey(
        "exams.QuestionOption",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    text_answer = models.TextField(blank=True)

    is_correct = models.BooleanField(default=False)

    marks_awarded = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )
