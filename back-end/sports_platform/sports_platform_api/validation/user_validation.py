from rest_framework import serializers
from generic_validators import english_dot



class User(serializers.Serializer):
   email = serializers.EmailField(required=True)
   surname = serializers.CharField(min_length = 2, max_length = 30, validators = [english_dot])
