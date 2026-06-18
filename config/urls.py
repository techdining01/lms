"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from apps.core.views.home import LandingPageView
from django.conf import settings
from django.http import HttpResponse, Http404
from pathlib import Path


def service_worker(request):
    """Serve the service worker file from the project's static folder at /sw.js

    This allows the service worker to be registered at the site root (scope '/').
    """
    sw_path = Path(settings.BASE_DIR) / "static" / "sw.js"
    if sw_path.exists():
        return HttpResponse(
            sw_path.read_text(encoding="utf-8"), content_type="application/javascript"
        )
    raise Http404


urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("sw.js", service_worker),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += [
    path("accounts/", include("apps.accounts.urls")),
    path("academics/", include("apps.academics.urls")),
    path("learning/", include("apps.learning.urls")),
    path("enrollment/", include("apps.enrollments.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("exams/", include("apps.exams.urls")),
    path("grades/", include("apps.grades.urls")),
    path("report-cards/", include("apps.report_cards.urls")),
    path("communication/", include("apps.communication.urls")),
    path(
        "__reload__/",
        include("django_browser_reload.urls"),
    ),
]
