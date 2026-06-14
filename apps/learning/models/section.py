from django.db import models


class Section(models.Model):
    course = models.ForeignKey(
        "learning.Course", on_delete=models.CASCADE, related_name="sections"
    )

    title = models.CharField(max_length=255)

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
