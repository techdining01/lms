from django.db import models


class ReportCard(models.Model):
    class Status(models.TextChoices):

        DRAFT = (
            "DRAFT",
            "Draft"
        )

        REVIEWED = (
            "REVIEWED",
            "Reviewed"
        )

        APPROVED = (
            "APPROVED",
            "Approved"
        )

        PUBLISHED = (
            "PUBLISHED",
            "Published"
        )

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    school_class = models.ForeignKey(
        "academics.SchoolClass",
        on_delete=models.CASCADE,
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.CASCADE,
    )

    total_score = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    average = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    attendance_percentage = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    position = models.PositiveIntegerField(default=0)

    teacher_remark = models.TextField(blank=True)

    principal_remark = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    generated_at = models.DateTimeField(auto_now_add=True)

    class_size = models.PositiveIntegerField(default=0)

