from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def notification_count(request):

    unread_count = request.user.notifications.filter(status="PENDING").count()

    return render(
        request,
        "communication/partials/unread_count.html",
        {"unread_count": unread_count},
    )
