from rest_framework import serializers

from generic_validators import english_dot, date, gender


class Sport_SkillLevel(serializers.Serializer):
    sport = serializers.IntegerField(min_value = 0, required=True)
    skill_level = serializers.IntegerField(min_value = 1, max_value = 5, required=True)

class User(serializers.Serializer):
   email = serializers.EmailField(required=True)
   familyName = serializers.CharField(min_length = 2, max_length = 30, validators = [english_dot])
   sports = serializers.ListField(child=Sport_SkillLevel())
   name = serializers.CharField(min_length=2, max_length = 30, validattors = [english_dot])
   date = serializers.DateField(validators = [date])
   gender =serializers.CharField(validators = [gender])

