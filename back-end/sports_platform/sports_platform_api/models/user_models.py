from django.db import models


class User(models.Model):
   user_id = models.BigAutoField(primary_key=True)
   email = models.EmailField()
   password = models.CharField(max_length=30)
   identifier = models.CharField(max_length=30)
   name = models.CharField(max_length=30,blank=True)
   familyName = models.CharField(max_length=30,blank=True)
   birthDate = models.DateField(blank=True, null=True)
   gender = models.SmallIntegerField(blank=True, null=True)


class SportSkillLevel(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    sport_id = models.ForeignKey('Sport', on_delete=models.CASCADE)
    skill_level = models.SmallIntegerField()


class Block(models.Model):
    blocker = models.ForeignKey('User', on_delete=models.CASCADE)
    blocked = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)