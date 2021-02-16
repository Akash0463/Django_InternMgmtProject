from django.contrib import admin
from .models import CustomUser, ApplicationDetails
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Fields',
            {
                'fields':(
                    'university',
                    'phone',
                )
            }
        )
    )

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ApplicationDetails)

