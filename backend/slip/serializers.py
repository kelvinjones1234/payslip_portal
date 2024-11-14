from rest_framework import serializers
from datetime import datetime
from .models import PaySlip

class PaySlipSerializer(serializers.ModelSerializer):
    generated_date = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = PaySlip
        fields = ['id', 'user', 'file', 'generated_date', 'display_name']
        read_only_fields = ['id', 'generated_date', 'display_name']

    def get_generated_date(self, obj):
        # Format the upload_date to 'Generated: <day> <month> <year>'
        return obj.upload_date.strftime("Generated: %d %B %Y")

    def get_display_name(self, obj):
        # Extract the month and year from the upload date to format as 'Payslip for <Month> <Year>'
        return f"Payslip for {obj.upload_date.strftime('%B %Y')}"
