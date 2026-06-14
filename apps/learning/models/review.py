from django.db import models


class Review(models.Model):
    learner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    course = models.ForeignKey("learning.Course", on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
