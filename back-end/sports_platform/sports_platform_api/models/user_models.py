from django.db import models

class User(models.Model):
    email = models.EmailField()
    surname = models.CharField()

class Sport_SkillLevel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.IntegerField()
    skill_level = models.IntegerField()