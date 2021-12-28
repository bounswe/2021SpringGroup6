from django.urls import path

from sports_platform_api.views import activity_stream_views

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
    path('activitystream', activity_stream_views.get_activity_stream),
    path('events/<int:event_id>', event_views.get_event),
    path('events/<int:event_id>/spectators', event_views.attend_spectator),
    path('events/<int:event_id>/interesteds', event_views.add_interest),
    path('events/<int:event_id>/participants', event_views.accept_participant),
    path('events/searches', event_views.search_event),
    path('users/<int:user_id>/participating', get_participating_events),
    path('users/<int:user_id>/spectating', get_spectating_events),
    path('users/<int:user_id>/interested', get_interested_events),
    path('events/<int:event_id>/badges', event_views.get_badges),
    path('users/<int:user_id>/badges', user_views.get_badges),
    path('badges', get_badges),
    path('notifications',user_views.notification),
    path('notifications/<int:notification_id>',user_views.read_notification),
    path('events/<int:event_id>/discussion', post_post),
    path('events/<int:event_id>/discussion/<int:post_id>', delete_post_post),
    path('events/<int:event_id>/discussion/<int:post_id>/comment/<int:comment_id>', delete_comment),
    path('users/searches', user_views.search_user)
]
