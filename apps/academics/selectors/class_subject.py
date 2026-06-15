from apps.academics.models import ClassSubject


def get_class_subjects():
    return ClassSubject.objects.select_related(
        "school_class",
        "subject",
        "teacher",
    )
