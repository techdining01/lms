import uuid

from django.db import models


class ResultVerification(models.Model):
    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
    )

    report_card = models.OneToOneField(
        "report_cards.ReportCard",
        on_delete=models.CASCADE,
    )
