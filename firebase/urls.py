from django.urls import path
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]