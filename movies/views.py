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
from .pagination import CustomPagination
from .filters import MovieFilter

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










