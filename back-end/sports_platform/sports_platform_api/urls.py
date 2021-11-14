from django.urls import path

from sports_platform_api.views import sport_views
from .views import *

urlpatterns = [
    path('users', user_views.create_user),
    path('users/login', user_views.login),
    path('sports', sport_views.get_sports),
    path('users/<int:user_id>', user_views.get_user),
    path('users/logout', user_views.logout)
]
