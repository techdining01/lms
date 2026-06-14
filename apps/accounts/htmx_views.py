from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import User
from .services.approval import approve_user





class ApproveUserView(View):
    def post(self, request, pk):

        user = get_object_or_404(User, pk=pk)

        approve_user(user, request.user)

        return render(request, "accounts/partials/user_row.html", {"user": user})
