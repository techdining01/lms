from django.db import models


class StudentEnrollment(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        TRANSFERRED = "TRANSFERRED", "Transferred"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"
        GRADUATED = "GRADUATED", "Graduated"

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="enrollments",
        limit_choices_to={
            "role": "STUDENT"
        },
    )

    session = models.ForeignKey(
        "academics.AcademicSession",
        on_delete=models.PROTECT,
    )

    school_class = models.ForeignKey(
        "academics.SchoolClass",
        on_delete=models.PROTECT,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        db_index=True,
    )

    enrolled_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_enrollments",
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-enrolled_at"]

    def __str__(self):
        return (
            f"{self.student} - "
            f"{self.school_class}"
        )