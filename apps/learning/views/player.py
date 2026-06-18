from django.views.generic import DetailView

from apps.learning.models.course import Course


class CoursePlayerView(DetailView):
    model = Course

    slug_field = "slug"

    slug_url_kwarg = "slug"

    template_name = "learning/player.html"

    context_object_name = "course"

    def get_queryset(self):
        return Course.objects.select_related(
            "instructor",
            "category",
        ).prefetch_related(
            "sections__lessons",
        )
