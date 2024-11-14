from django.urls import path
from .views import DepartmentListView


urlpatterns = [
  path('depatements/', DepartmentListView.as_view(), name='departments'),
]