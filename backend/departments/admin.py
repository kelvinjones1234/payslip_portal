from django.contrib import admin

from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the admin list view
    search_fields = ('name',)  # Add search functionality by department name

# Register both User and Department models
admin.site.register(Department, DepartmentAdmin)