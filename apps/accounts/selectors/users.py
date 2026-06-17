from apps.accounts.models.user import User


def get_pending_users():
    return User.objects.filter(status="PENDING")


def get_active_users():
    return User.objects.filter(status="ACTIVE")


def get_teachers():
    return User.objects.filter(role="TEACHER")


def get_students():
    return User.objects.filter(role="STUDENT")
