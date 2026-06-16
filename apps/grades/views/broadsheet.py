from django.views.generic import TemplateView

from apps.grades.selectors.broadsheet import get_broadsheet

class BroadsheetView(TemplateView):
    template_name = "grades/broadsheet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["results"] = get_broadsheet(
            self.kwargs["class_id"],
            self.kwargs["term_id"],
        )

        return context