from django.db import models


class AttendanceRecord(models.Model):
    class Status(models.TextChoices):
        PRESENT = ("PRESENT", "Present")

        ABSENT = ("ABSENT", "Absent")

        LATE = ("LATE", "Late")

        EXCUSED = ("EXCUSED", "Excused")

    session = models.ForeignKey(
        "attendance.AttendanceSession",
        on_delete=models.CASCADE,
        related_name="records",
    )

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PRESENT,
    )

    remark = models.TextField(blank=True)
