from django.urls import path
from .views import *

urlpatterns = [
    path('users/<int:user_id>', user_views.get_user)
]