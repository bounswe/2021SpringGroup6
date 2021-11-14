from django.urls import path
from .views import *

urlpatterns = [
    path('users', user_views.create_user),
    path('users/login', user_views.login),
    path('users/logout', user_views.logout),
    path('users/recover', user_views.forgot_password)
    path('users/<int:user_id>', user_views.get_user)
]
