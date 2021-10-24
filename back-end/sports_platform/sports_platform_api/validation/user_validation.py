from rest_framework import serializers
from generic_validators import english_dot



class User(serializers.Serializer):
   email = serializers.EmailField(required=True)
