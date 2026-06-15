from django.db import models


class SubmissionAttachment(models.Model):
    submission = models.ForeignKey(
        "assignments.AssignmentSubmission",
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    file = models.FileField(upload_to="assignments/submissions/")
