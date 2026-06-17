from django.db import models


class AttendanceSummary(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.CASCADE,
    )

    total_days = models.PositiveIntegerField(default=0)

    present_days = models.PositiveIntegerField(default=0)

    absent_days = models.PositiveIntegerField(default=0)

    late_days = models.PositiveIntegerField(default=0)

    attendance_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )
