from django.db import models


class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", "Beginner"
        INTERMEDIATE = "INTERMEDIATE", "Intermediate"
        ADVANCED = "ADVANCED", "Advanced"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        UNDER_REVIEW = "UNDER_REVIEW", "Under_Review"
        PUBLISHED = "PUBLISHED", "Published"
        ARCHIVED = "ARCHIVED", "Archived"

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    instructor = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="courses"
    )

    category = models.ForeignKey(
        "learning.Category", on_delete=models.PROTECT, related_name="courses"
    )

    thumbnail = models.ImageField(upload_to="courses/")

    description = models.TextField()

    level = models.CharField(max_length=20, choices=Level.choices)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
