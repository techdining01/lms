from django.utils import timezone


def approve_user(user, approver):

    user.status = "ACTIVE"
    user.approved_by = approver
    user.approved_at = timezone.now()

    user.save()


def suspend_user(user):

    user.status = "SUSPENDED"
    user.save()


def reject_user(user):

    user.status = "REJECTED"
    user.save()
