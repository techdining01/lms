from django.db import transaction

from apps.academics.models import AcademicSession


@transaction.atomic
def set_current_session(session):

    AcademicSession.objects.update(is_current=False)

    session.is_current = True

    session.save(update_fields=["is_current"])

    return session
