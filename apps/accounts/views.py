from django.shortcuts import redirect
from apps.accounts.models.user import User
from django.views import View
from .services.dashboard import DashboardRouter
from django.views.generic import ListView


class DashboardRedirectView(View):
    def get(self, request):

        return redirect(DashboardRouter.get_dashboard(request.user))
    
class UserListView(ListView):
    model = User

    paginate_by = 20

    template_name = "accounts/user_list.html"

