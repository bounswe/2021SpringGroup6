from django.urls import path
from .views import *

urlpatterns = [
    path('users', user_views.create_user)
]
