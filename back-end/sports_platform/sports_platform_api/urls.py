from django.urls import path
from .views import *

urlpatterns = [
    path('users', user_views.create_user),
    path('users/login', user_views.login),
    path('users/logout', user_views.logout)
]
