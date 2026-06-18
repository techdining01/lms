from django import forms
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm

from apps.accounts.models import StudentProfile


User = get_user_model()


class CustomSignupForm(SignupForm):
    """Custom signup form that sets a default role and creates a StudentProfile."""

    role = forms.ChoiceField(
        choices=User.Role.choices,
        initial=User.Role.STUDENT,
        widget=forms.HiddenInput(),
        required=False,
    )

    def save(self, request):
        user = super().save(request)

        # Persist role if provided (default to STUDENT)
        role = self.cleaned_data.get("role") or User.Role.STUDENT
        user.role = role
        user.save()

        # Ensure StudentProfile exists for students
        if role == User.Role.STUDENT:
            StudentProfile.objects.get_or_create(
                user=user,
                defaults={"admission_number": f"S{user.id:04d}"},
            )

        return user
