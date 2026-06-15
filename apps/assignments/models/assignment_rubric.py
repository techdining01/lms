from django.db import models


class AssignmentRubric(models.Model):
    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="rubrics",
    )

    criteria = models.CharField(max_length=255)

    max_score = models.PositiveIntegerField()
