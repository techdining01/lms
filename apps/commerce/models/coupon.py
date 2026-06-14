from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)

    percentage = models.PositiveIntegerField()

    active = models.BooleanField(default=True)

    expires_at = models.DateTimeField(null=True, blank=True)
