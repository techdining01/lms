from django.db import models


class AssignmentAttachment(models.Model):
    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    file = models.FileField(upload_to="assignments/resources/")

    uploaded_at = models.DateTimeField(auto_now_add=True)
