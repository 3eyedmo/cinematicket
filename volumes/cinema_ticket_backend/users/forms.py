from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CinemaTicketUser


class CustomUserCreationForm(forms.ModelForm):
    """Form for creating new users, including password validation"""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CinemaTicketUser
        fields = ("email", "username")

    def clean_password2(self):
        """Ensure passwords match"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        """Save user with hashed password"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """Form for updating existing users"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CinemaTicketUser
        fields = ("email", "username", "password", "is_active", "is_admin", "is_staff")
