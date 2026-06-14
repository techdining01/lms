from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        PARENT = "PARENT", "Parent"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        LEARNER = "LEARNER", "Learner"

    class UserStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"
        REJECTED = "REJECTED", "Rejected"

    role = models.CharField(max_length=20, choices=Role.choices)

    phone_number = models.CharField(max_length=20, blank=True)

    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.PENDING,
        db_index=True,
    )

    approved_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_users",
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name() or self.username



class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    admission_number = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



