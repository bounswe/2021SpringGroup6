from rest_framework import serializers

from .generic_validators import english_dot, date, gender, password, english_dot_number


class Sport_SkillLevel(serializers.Serializer):
    sport = serializers.IntegerField(min_value = 0, required=True)
    skill_level = serializers.IntegerField(min_value = 1, max_value = 5, required=True)

class User(serializers.Serializer):
   email = serializers.EmailField(required=True)
   identifier = serializers.CharField(min_length = 3, max_length = 15, validators = [english_dot_number])
   familyName = serializers.CharField(min_length = 2, max_length = 30, validators = [english_dot])
   sports = serializers.ListField(child=Sport_SkillLevel())
   name = serializers.CharField(min_length=2, max_length = 30, validators = [english_dot])
   date = serializers.DateField(validators = [date])
   gender =serializers.CharField(validators = [gender])

class Login(serializers.Serializer):
    identifier = serializers.CharField(min_length = 3, max_length = 15, validators = [english_dot_number])
    password = serializers.CharField(min_length = 8, max_length = 15, validators = [password])

class Block(serializers.Serializer):
    date = serializers.DateField(validators = [date])