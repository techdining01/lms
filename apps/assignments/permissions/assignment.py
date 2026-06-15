from apps.core.constants.roles import EDUCATOR_ROLES


def can_manage_assignment(user):

    return user.is_authenticated and user.role in EDUCATOR_ROLES


def can_submit_assignment(user):

    return user.is_authenticated and user.role in [
        "STUDENT",
        "LEARNER",
    ]
