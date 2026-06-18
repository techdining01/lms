from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.core.services.dashboard_service import DashboardService


@login_required
def dashboard(request):

    context = DashboardService.get_dashboard_context(request.user)

    return render(
        request,
        "pages/dashboard/index.html",
        context,
    )
