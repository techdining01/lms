from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, StudentProfile, TeacherProfile, ParentProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if not created:
        return

    if instance.role == User.Role.STUDENT:
        StudentProfile.objects.create(
            user=instance, admission_number=f"STD-{instance.id}"
        )

    elif instance.role == User.Role.TEACHER:
        TeacherProfile.objects.create(user=instance, employee_id=f"TCH-{instance.id}")

    elif instance.role == User.Role.PARENT:
        ParentProfile.objects.create(user=instance)
