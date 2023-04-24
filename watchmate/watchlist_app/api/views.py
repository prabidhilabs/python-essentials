from rest_framework.response import Response
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies)
    return Response(serializer.data)