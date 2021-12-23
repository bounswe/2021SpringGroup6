from rest_framework import serializers
from ..models.user_models import User

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        exclude = ['password', 'last_login']