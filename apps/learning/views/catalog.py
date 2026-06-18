from django.views.generic import ListView

from apps.learning.models.course import Course


class CourseCatalogView(ListView):
    model = Course
    template_name = "learning/catalog.html"
    context_object_name = "courses"
    paginate_by = 12

    def get_queryset(self):
        queryset = Course.objects.filter(
            status=Course.Status.PUBLISHED
        )
        q = self.request.GET.get("q")

        if q:
            queryset = queryset.filter(title__icontains=q)

        return queryset
