from rest_framework import serializers

from .generic_validators import english_dot, date, gender, password, english_dot_number


class Sport_SkillLevel(serializers.Serializer):
    sport = serializers.CharField(required=True)
    skill_level = serializers.IntegerField(min_value = 1, max_value = 5, required=True)


class User(serializers.Serializer):
   email = serializers.EmailField(required=True)
   identifier = serializers.CharField(required=True, min_length = 3, max_length = 15, validators = [english_dot_number])
   familyName = serializers.CharField(required=False,min_length = 2, max_length = 30, validators = [english_dot])
   sports = serializers.ListField(child=Sport_SkillLevel(), required=False)
   name = serializers.CharField(required=False,min_length=2, max_length = 30, validators = [english_dot])
   birthDate = serializers.DateField(required=False, validators = [date])
   gender =serializers.CharField(required=False, validators = [gender])
   password = serializers.CharField(min_length = 8, max_length = 15, validators = [password], required = True)
   email_visibility = serializers.BooleanField(required=False)
   name_visibility = serializers.BooleanField(required=False)
   familyName_visibility = serializers.BooleanField(required=False)
   birthDate_visibility = serializers.BooleanField(required=False)
   gender_visibility = serializers.BooleanField(required=False)

class Update(serializers.Serializer):
   email = serializers.EmailField(required=False)
   familyName = serializers.CharField(required=False,min_length = 2, max_length = 30, validators = [english_dot])
   sports = serializers.ListField(required=False, child=Sport_SkillLevel())
   name = serializers.CharField(required=False,min_length=2, max_length = 30, validators = [english_dot])
   birthDate = serializers.DateField(required=False, validators = [date])
   gender =serializers.CharField(required=False, validators = [gender])

class Login(serializers.Serializer):
    identifier = serializers.CharField(min_length = 3, max_length = 15, validators = [english_dot_number], required= True)
    password = serializers.CharField(min_length = 8, max_length = 15, validators = [password], required = True)

class Block(serializers.Serializer):
    user_id =  serializers.IntegerField(min_value = 1, max_value = 9223372036854775807)

class Follow(serializers.Serializer):
    user_id = serializers.IntegerField(min_value = 1, max_value = 9223372036854775807)


class Recover(serializers.Serializer):
    email = serializers.EmailField(required=True)

class Set_Visibility(serializers.Serializer):
    email_visibility = serializers.BooleanField(required=False)
    name_visibility = serializers.BooleanField(required=False)
    familyName_visibility = serializers.BooleanField(required=False)
    birthDate_visibility = serializers.BooleanField(required=False)
    gender_visibility = serializers.BooleanField(required=False)

class Badge(serializers.Serializer):
    badge = serializers.CharField(min_length=3, max_length=100, validators=[
                                  english_dot_number], required=True)

class Search(serializers.Serializer):
    name = serializers.CharField(required=False)
    familyName = serializers.CharField(required=False)
    identifier = serializers.CharField(required=False)

    def validate(self, data):
        if len(data) != 1:
            raise serializers.ValidationError({"nameContains": "Exactly 1 filter should be provided. Options are name, familyName and identifier"})