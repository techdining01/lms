from django.db import models


class StudentAttendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "PRESENT"
        ABSENT = "ABSENT"
        LATE = "LATE"

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    school_class = models.ForeignKey(
        "academics.SchoolClass",
        on_delete=models.CASCADE,
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
    )

    marked_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="attendance_marked",
    )

    class Meta:
        unique_together = (
            "student",
            "date",
        )
