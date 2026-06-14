from django.views.generic import ListView
from django.views.generic import DetailView

from apps.learning.models import Course


class CourseCatalogView(ListView):
    model = Course

    paginate_by = 12

    template_name = "learning/catalog.html"

    queryset = Course.objects.filter(is_published=True).select_related(
        "category",
        "instructor",
    )


class CourseDetailView(DetailView):
    model = Course

    slug_field = "slug"

    template_name = "learning/course_detail.html"
