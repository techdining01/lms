from django.utils import timezone

from apps.course_delivery.models.progress import LessonProgress


def mark_completed(
    student,
    lesson,
):

    obj, created = LessonProgress.objects.get_or_create(
        student=student,
        lesson=lesson,
    )

    obj.status = LessonProgress.Status.COMPLETED

    obj.completed_at = timezone.now()

    obj.save()

    return obj
