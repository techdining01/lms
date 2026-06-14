from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    slug = models.SlugField(unique=True)

    icon = models.CharField(max_length=100, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
