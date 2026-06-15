from apps.exams.models import Exam


def published_exams():

    return Exam.objects.filter(is_published=True)
