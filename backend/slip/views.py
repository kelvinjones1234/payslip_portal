from rest_framework import generics
from .models import PaySlip
from .serializers import PaySlipSerializer
from rest_framework.permissions import IsAuthenticated

class PaySlipListView(generics.ListAPIView):
    serializer_class = PaySlipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the PaySlip objects for the current logged-in user
        return PaySlip.objects.filter(user=self.request.user)
