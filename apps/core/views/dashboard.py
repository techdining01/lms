from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "pages/dashboard/index.html"

    def get_context_data(
        self,
        **kwargs,
    ):
        context = super().get_context_data(**kwargs)

        context.update(
            {
                "student_count": 0,
                "course_count": 0,
                "exam_count": 0,
                "attendance_count": 0,
            }
        )

        return context
