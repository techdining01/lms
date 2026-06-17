from django.db import models


class AttendanceSession(models.Model):
    school_class = models.ForeignKey(
        "academics.SchoolClass",
        on_delete=models.CASCADE,
    )

    date = models.DateField()

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "school_class",
            "date",
        )
