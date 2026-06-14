from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        FAILED = "FAILED", "Failed"
        REFUNDED = "REFUNDED", "Refunded"

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
