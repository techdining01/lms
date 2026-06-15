from django.db import models


class Question(models.Model):
    class QuestionType(models.TextChoices):
        MCQ = "MCQ"

        TRUE_FALSE = "TRUE_FALSE"

        FILL_BLANK = "FILL_BLANK"

        SHORT_ANSWER = "SHORT_ANSWER"

        ESSAY = "ESSAY"

    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question_text = models.TextField()

    question_type = models.CharField(
        max_length=30,
        choices=QuestionType.choices,
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
    )

    explanation = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)
