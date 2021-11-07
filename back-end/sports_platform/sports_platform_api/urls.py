from django.urls import path
from .views import *

urlpatterns = [
    path('users/login', user_views.login),
    path('users/<int:user_id>/follow', user_views.follow_user),
    path('users/<int:user_id>/unfollow', user_views.unfollow_user),
]