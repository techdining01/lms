from apps.academics.models import Subject


def get_subjects():
    return Subject.objects.filter(is_active=True)
