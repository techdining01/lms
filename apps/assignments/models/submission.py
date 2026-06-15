from django.db import models


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="assignment_submissions",
    )

    text_answer = models.TextField(blank=True)

    attempt_number = models.PositiveIntegerField(default=1)

    is_late = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]
