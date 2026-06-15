from apps.academics.models import AcademicSession


def get_current_session():
    return AcademicSession.objects.filter(is_current=True).first()


def get_sessions():
    return AcademicSession.objects.all()
