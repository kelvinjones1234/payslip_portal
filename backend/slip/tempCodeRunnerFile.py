from django.db import models
from users.models import User

class PaySlip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pay_slips")
    file = models.FileField(upload_to="payslips/")
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pay Slip for {self.user.username}"