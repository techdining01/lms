from django.db import models


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    order = models.OneToOneField("commerce.Order", on_delete=models.CASCADE)

    reference = models.CharField(max_length=255, unique=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    provider = models.CharField(max_length=50, default="PAYSTACK")

    created_at = models.DateTimeField(auto_now_add=True)
