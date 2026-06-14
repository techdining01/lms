from django.db import models


class ClassSubject(models.Model):
    school_class = models.ForeignKey(
        "academics.SchoolClass", on_delete=models.CASCADE, related_name="class_subjects"
    )

    subject = models.ForeignKey(
        "academics.Subject", on_delete=models.CASCADE, related_name="subject_classes"
    )

    teacher = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "TEACHER"},
    )

    class Meta:
        unique_together = (
            "school_class",
            "subject",
        )

    def __str__(self):
        return f"{self.school_class} - {self.subject}"
