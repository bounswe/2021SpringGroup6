from django.db import models

class Sport(models.Model):
    class Meta:
        db_table = 'sport'

    name = models.CharField(primary_key=True, max_length=30)