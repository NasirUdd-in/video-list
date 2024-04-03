from django.urls import path
from .views import CustomUserAPIView,UserLoginAPIView,MovieCreateAPIView,RatingListCreateAPIView
from .views import AllRatings

urlpatterns = [
    path('users/', CustomUserAPIView.as_view(), name='user-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('add-movies/', MovieCreateAPIView.as_view(), name='movie-create'),
    path('ratings/', RatingListCreateAPIView.as_view(), name='rating-list-create'),
    path('all-ratings/', AllRatings.as_view(), name='all-ratings'),

]
