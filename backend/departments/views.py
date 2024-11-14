from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer