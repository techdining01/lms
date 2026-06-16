from django.db import models


class ExamQuestion(models.Model):
    exam = models.ForeignKey(
        "exams.Exam",
        on_delete=models.CASCADE,
        related_name="exam_questions",
    )

    question = models.ForeignKey(
        "exams.QuestionBank",
        on_delete=models.CASCADE,
    )

    order = models.PositiveIntegerField(default=0)

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
    )

    class Meta:
        ordering = ["order"]
