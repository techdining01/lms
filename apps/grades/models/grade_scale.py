from django.db import models


class GradeScale(models.Model):
    grade = models.CharField(max_length=5)

    min_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    max_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    remark = models.CharField(max_length=100)

    points = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["-min_score"]

    def __str__(self):
        return self.grade
