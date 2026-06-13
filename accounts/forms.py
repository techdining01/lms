from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)

    remember_me = forms.BooleanField(required=False)

    def clean(self):

        cleaned_data = super().clean()

        username = cleaned_data.get("username")

        password = cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Invalid credentials")

        cleaned_data["user"] = user

        return cleaned_data
