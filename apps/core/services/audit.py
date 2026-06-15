from apps.core.models import AuditLog


def log_action(
    *,
    actor,
    action,
    object_id,
    content_type,
):

    AuditLog.objects.create(
        actor=actor,
        action=action,
        object_id=object_id,
        content_type=content_type,
    )
