from django.db import transaction

from apps.academics.models import Term


@transaction.atomic
def set_current_term(term):

    Term.objects.filter(session=term.session).update(is_current=False)

    term.is_current = True

    term.save(update_fields=["is_current"])

    return term
