from django.contrib import admin
from django.urls import include, path
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('devices', FCMDeviceAuthorizedViewSet)


urlpatterns = [
    path('swagger/', include('swagger.urls')),
    #path('api/v1/movies/moviesTitles/', include('movies.urls')),
    #path('api/v1/movies/id/', include('movies.urls')),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/file/', include('file_upload.urls')),
    path('', include('firebase.urls')),
]
