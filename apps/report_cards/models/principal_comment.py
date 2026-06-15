from django.db import models


class PrincipalComment(models.Model):
    report_card = models.OneToOneField(
        "report_cards.ReportCard",
        on_delete=models.CASCADE,
    )

    comment = models.TextField()
