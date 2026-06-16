from django.contrib.auth import models



class PsychomotorTrait(models.Model):
    report_card = models.ForeignKey(
        "report_cards.ReportCard",
        on_delete=models.CASCADE,
    )

    handwriting = models.PositiveSmallIntegerField(default=0)

    sports = models.PositiveSmallIntegerField(default=0)

    creativity = models.PositiveSmallIntegerField(default=0)
