from django.urls import path
from django.conf import settings
from .views import PaySlipListView
from django.conf.urls.static import static


urlpatterns = [
  path('api/slips/', PaySlipListView.as_view(), name='slip'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)