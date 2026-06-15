from django.db import models


class AssignmentGrade(models.Model):
    submission = models.OneToOneField(
        "assignments.AssignmentSubmission",
        on_delete=models.CASCADE,
        related_name="grade",
    )

    raw_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    penalty_applied = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    final_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    feedback = models.TextField(blank=True)

    graded_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    graded_at = models.DateTimeField(
        auto_now_add=True,
    )

