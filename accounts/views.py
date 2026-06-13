from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import FormView
from .forms import LoginForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    template_name = "accounts/login.html"

    form_class = LoginForm

    def form_valid(self, form):

        user = form.cleaned_data["user"]

        login(self.request, user)

        if not form.cleaned_data.get("remember_me"):
            self.request.session.set_expiry(0)

        return redirect("dashboard_redirect")


class LogoutView(View):
    def get(self, request):

        logout(request)

        return redirect("login")


class DashboardRedirectView(LoginRequiredMixin, View):
    def get(self, request):

        role = request.user.role

        if role == "ADMIN":
            return redirect("admin_dashboard")

        elif role == "TEACHER":
            return redirect("teacher_dashboard")

        elif role == "STUDENT":
            return redirect("student_dashboard")

        elif role == "PARENT":
            return redirect("parent_dashboard")

        return redirect("login")
