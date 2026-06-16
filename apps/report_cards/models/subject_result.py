from django.db import models


class SubjectResult(models.Model):
    report_card = models.ForeignKey(
        "report_cards.ReportCard",
        on_delete=models.CASCADE,
        related_name="subjects",
    )

    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
    )

    assignment_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    ca_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    exam_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    total = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    grade = models.CharField(max_length=5)

    remark = models.CharField(max_length=100)
