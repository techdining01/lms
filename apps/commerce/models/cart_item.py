from django.db import models


class CartItem(models.Model):
    cart = models.ForeignKey(
        "commerce.Cart", on_delete=models.CASCADE, related_name="items"
    )

    course = models.ForeignKey("learning.Course", on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (
            "cart",
            "course",
        )
