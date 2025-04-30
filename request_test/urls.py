from django.urls import path
from .views import request_info_view
from .views import file_upload_view

urlpatterns = [
  path('request-info/', request_info_view, name='request_info'),
  path('upload/', file_upload_view, name='upload_file'),
]