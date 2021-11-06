from django.urls import path
from .views import *

urlpatterns = [
    path('users/login', user_views.login)
]