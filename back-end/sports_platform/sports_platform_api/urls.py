from django.urls import path
from .views import *

urlpatterns = [
    path('users', user_views.create_user),
    path('users/login', user_views.login), 
    path('users/<int:user_id>', user_views.get_user),
    path('users/logout', user_views.logout)
]
