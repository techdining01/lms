from django.db import models


class AcademicSession(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )

    is_current = models.BooleanField(default=False)

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.name
