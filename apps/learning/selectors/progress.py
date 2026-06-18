from apps.learning.models.progress import LessonProgress



def get_continue_learning(user):

    return (
        LessonProgress.objects.filter(student=user)
        .select_related("course")
        .order_by("-updated_at")
    )



def calculate_course_progress(
    learner,
    course,
):
    total = (
        course.sections.all()
        .values_list(
            "lessons",
            flat=True,
        )
        .count()
    )

    completed = LessonProgress.objects.filter(
        learner=learner,
        lesson__section__course=course,
        completed=True,
    ).count()

    if total == 0:
        return 0

    return round(completed / total * 100)