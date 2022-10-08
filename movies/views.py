from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .serializers import MovieTitleSerializer
from .serializers import MovieIdSerializer
from .serializers import MovieGenreSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from aiohttp import web
from django.apps import apps
from django.core.serializers import serialize
from mymoviedb.utils import database_sync_to_async

routes = web.RouteTableDef()

class ListIdMovieApiView(ListCreateAPIView):
    serializer_class = MovieIdSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ['id']

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)



class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ListTitleMovieApiView(ListCreateAPIView):
    serializer_class = MovieTitleSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]



class ListTitleMovieApiView(ListCreateAPIView):
    serializer_class = MovieGenreSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]


#@routes.view('/movies')
class MoviesListView(web.View):
    model = 'movies.Movie'

    async def get_queryset(self, **kwargs):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.all)()

    async def get(self):
        queryset = await self.get_queryset()
        text = serialize('json', queryset)
        return web.json_response(text=text)




