from django.db import models


class QuestionBankOption(models.Model):
    question = models.ForeignKey(
        "exams.QuestionBank",
        on_delete=models.CASCADE,
        related_name="options",
    )

    option_text = models.CharField(max_length=500)

    is_correct = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)
