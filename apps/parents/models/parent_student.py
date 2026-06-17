from django.db import models


class ParentStudent(models.Model):
    parent = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, limit_choices_to={"role": "PARENT"}
    )

    student = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, limit_choices_to={"role": "STUDENT"}
    )

    relationship = models.CharField(max_length=50)
