from django.urls import path, include
# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import (StreamPlatformAV, WatchListAV,
                                  WatchDetailAV, StreamPlatformDetailAV,ReviewList,
                                  ReviewDetail)


urlpatterns = [
    # # path('list/', movie_list, name='movie-list'),
     path('list/', WatchListAV.as_view(), name='movie-list'),
    # # path('<int:pk>', movie_details, name='movie-detail'),
     path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
     path('stream/', StreamPlatformAV.as_view(), name='stream'),
     path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
     path('review/',ReviewList.as_view(), name='review-list'),
     path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail')
     
]
