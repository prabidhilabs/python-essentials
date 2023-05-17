from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import (
    StreamPlatformAV,
    StreamPlatformLM,
    WatchListAV,
    WatchDetailAV,
    ReviewCreate,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    UserReview,
    WatchListGV,
)

router = DefaultRouter()
router.register("stream", StreamPlatformLM, basename="streamplatform")


urlpatterns = [
    # # path('list/', movie_list, name='movie-list'),
    path("list/", WatchListAV.as_view(), name="movie-list"),
    # # path('<int:pk>', movie_details, name='movie-detail'),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
    path("list2/", WatchListGV.as_view(), name="watch-list"),
    path("", include(router.urls)),
    #  path('stream/', StreamPlatformAV.as_view(), name='stream'),
    #  path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    #  path('review/',ReviewList.as_view(), name='review-list'),
    #  path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    #  path("review/<str:username>/", UserReview.as_view(), name="user-review-detail"),
    path("reviews/", UserReview.as_view(), name="user-review-detail"),
]
