from django.db import models


class Enrollment(models.Model):
    learner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    course = models.ForeignKey("learning.Course", on_delete=models.CASCADE)

    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "learner",
            "course",
        )
