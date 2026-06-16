from django.contrib.auth import models



class AffectiveTrait(models.Model):
    report_card = models.ForeignKey(
        "report_cards.ReportCard",
        on_delete=models.CASCADE,
    )

    punctuality = models.PositiveSmallIntegerField(default=0)

    honesty = models.PositiveSmallIntegerField(default=0)

    leadership = models.PositiveSmallIntegerField(default=0)

    cooperation = models.PositiveSmallIntegerField(default=0)

