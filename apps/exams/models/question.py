from django.db import models


class Question(models.Model):
    class QuestionType(models.TextChoices):
        MCQ = "MCQ"
        ESSAY = "ESSAY"
        TRUE_FALSE = "TRUE_FALSE"

    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
        related_name="questions",
    )

    text = models.TextField()

    question_type = models.CharField(
        max_length=20,
        choices=QuestionType.choices,
        default=QuestionType.MCQ,
    )

    marks = models.PositiveIntegerField(default=1)
