from django.conf import settings
from django.db import models


class QuestionBank(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "EASY", "Easy"
        MEDIUM = "MEDIUM", "Medium"
        HARD = "HARD", "Hard"

    class QuestionType(models.TextChoices):
        MCQ = "MCQ", "Multiple Choice"
        TRUE_FALSE = "TRUE_FALSE", "True False"
        FILL_BLANK = "FILL_BLANK", "Fill Blank"
        SHORT_ANSWER = "SHORT_ANSWER", "Short Answer"
        ESSAY = "ESSAY", "Essay"

    title = models.CharField(
        max_length=255,
        blank=True,
    )

    question_text = models.TextField()

    question_type = models.CharField(
        max_length=30,
        choices=QuestionType.choices,
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="question_bank",
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        "learning.Course",
        on_delete=models.CASCADE,
        related_name="question_bank",
        null=True,
        blank=True,
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
    )

    explanation = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text[:60]
