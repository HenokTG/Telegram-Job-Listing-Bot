from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ClientProfile, ApplicantProfile

from django.utils.translation import gettext_lazy as _


class UserAdminConfig(UserAdmin):
    
    model = ClientProfile
    
    search_fields = ('email', 'client_name', 'first_name',
                     'business_name', 'phone')
    list_filter = ('client_name', 'email', 'first_name',
                   'last_name', 'business_name',
                   'phone', 'is_active', 'is_staff')
    
    ordering = ('-date_joined',)
    
    list_display = ('client_name', 'email', 'charge_amount_per_job_post', 'first_name', 'last_name',
                    'business_name', 'phone', 'is_active')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {
         "fields": ("client_name", "first_name", "last_name")}),
        ('Business info', {'fields': ('business_name', 'charge_amount_per_job_post', 'description',
         'phone', "region", "zone", "woreda", "street",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
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

    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(ClientProfile, UserAdminConfig)
admin.site.register(ApplicantProfile)
