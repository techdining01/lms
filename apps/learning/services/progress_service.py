from django.utils import timezone

from apps.learning.models.progress import (
    LessonProgress,
)


class ProgressService:
    @staticmethod
    def complete_lesson(
        learner,
        lesson,
    ):
        progress, _ = LessonProgress.objects.get_or_create(
            learner=learner,
            lesson=lesson,
        )

        progress.completed = True

        progress.completed_at = timezone.now()

        progress.save()

        return progress
