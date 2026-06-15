from django.db import models


class RubricScore(models.Model):
    grade = models.ForeignKey(
        "assignments.AssignmentGrade",
        on_delete=models.CASCADE,
        related_name="rubric_scores",
    )

    rubric = models.ForeignKey(
        "assignments.AssignmentRubric",
        on_delete=models.CASCADE,
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
