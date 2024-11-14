from django.contrib import admin
from .models import PaySlip

class PaySlipAdmin(admin.ModelAdmin):
    list_display = ("user", "upload_date", "file")
    search_fields = ("user__username", "upload_date")
    list_filter = ("upload_date",)

admin.site.register(PaySlip, PaySlipAdmin)
