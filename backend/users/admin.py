from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class UserAdmin(BaseUserAdmin):
    # Define the fields to display in the admin interface
    list_display = ('email', 'full_name', 'title', 'gender', 'level', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender', 'level')
    search_fields = ('email', 'full_name', 'ippis_number')
    ordering = ('email',)

    # Fields to display when editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('full_name', 'title', 'gender', 'phone', 'ippis_number')}),
        (_('Department and Level'), {'fields': ('level', 'department')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Fields to display when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'title', 'gender', 'phone', 'ippis_number', 'level', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, UserAdmin)
