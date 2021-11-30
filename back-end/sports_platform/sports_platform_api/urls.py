from django.urls import path

from .views import *

urlpatterns = [
    path('users/login', user_views.login),
    path('users/<int:user_id>/following', user_views.follow_user),
    path('users/<int:user_id>/follower', user_views.get_follower),
    path('users', user_views.create_user),
    path('sports', sport_views.get_sports),
    path('users/<int:user_id>', user_views.get_user),
    path('users/logout', user_views.logout),
    path('users/recover', user_views.forgot_password),
    path('users/<int:user_id>/blocked', user_views.block_user),
    path('users/<user_id>/visible_attributes', user_views.set_visibility),

    path('events', event_views.create_event),
    path('events/<int:event_id>/spectators', event_views.attend_spectator),
]
