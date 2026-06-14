from django.db import models


class Term(models.Model):
    class TermChoices(models.TextChoices):
        FIRST = "FIRST", "First Term"
        SECOND = "SECOND", "Second Term"
        THIRD = "THIRD", "Third Term"

    session = models.ForeignKey(
        "academics.AcademicSession", on_delete=models.CASCADE, related_name="terms"
    )

    name = models.CharField(max_length=20, choices=TermChoices.choices)

    is_current = models.BooleanField(default=False)

    start_date = models.DateField()

    end_date = models.DateField()

    class Meta:
        unique_together = (
            "session",
            "name",
        )

    def __str__(self):
        return f"{self.get_name_display()}"
