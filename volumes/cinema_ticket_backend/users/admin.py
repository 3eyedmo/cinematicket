from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CinemaTicketUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CinemaTicketUser

    list_display = ("email", "username", "is_admin", "is_staff", "is_active")
    list_filter = ("is_admin", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Permissions",
            {"fields": ("is_admin", "is_staff", "is_active", "is_superuser")},
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_admin",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ("email", "username")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(CinemaTicketUser, CustomUserAdmin)
