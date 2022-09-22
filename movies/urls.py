from django.urls import path

from .views import ListTitleMovieApiView, ListIdMovieApiView, ListCreateMovieAPIView, RetrieveUpdateDestroyMovieAPIView

urlpatterns = [
    path('moviesTitles/', ListTitleMovieApiView.as_view(), name='get_post_movies_titles'),
    path('movies/id/', ListIdMovieApiView.as_view(), name='get_post_movies_id'),
    path('movies/', ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('', RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]