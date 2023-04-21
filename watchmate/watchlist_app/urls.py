from django.urls import path
from watchlist_app import views
from . import views


urlpatterns = [
    
    path('movie_list/', views.movie_list, name="movie-list" ),
]
 