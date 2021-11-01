from django.db import models

class Sport(models.Model):
    class Meta:
        db_table = 'sport'

    sport_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)