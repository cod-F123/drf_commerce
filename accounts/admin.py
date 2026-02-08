from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , UserAddress
from django.utils.translation import gettext_lazy as _


# Register your models here.

class UserAddressInlineAdmin(admin.StackedInline):
    model = UserAddress
    extra = 1
    verbose_name_plural = "User Addresses"

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","usable_password", "password1", "password2"),
            },
        ),
    )

    list_display = ("email", "username",  "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email", "username")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    inlines = [UserAddressInlineAdmin]

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["zip_code","user__email"]
