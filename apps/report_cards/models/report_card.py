from django.db import models


class ReportCard(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.CASCADE,
    )

    average_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    position = models.PositiveIntegerField(default=0)

    generated_at = models.DateTimeField(auto_now_add=True)
