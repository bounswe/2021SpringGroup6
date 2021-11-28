from django.db import models


creator: int
name: string
time: string
date: string
latitude: double
longitude: double
minParticipants: int
totalSpectators: string
maxParticipants: int
description: string
minSkillLevel: int

class Event(models.Model):
    class Meta:
        db_table = 'event'

    event_id = models.BigAutoField(primary_key=True)
    name = models.CharField(primary_key=True, max_length=100, primary_key=True)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    organizer = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    
    startDate = models.DateTimeField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField()
    district = models.CharField()

    minimumattendeecapacity = models.IntegerField(min_value=0)
    maximumattendeecapacity = models.IntegerField()
    maxspectatorcapacity = models.IntegerField()
    minskilllevel = models.IntegerField()
    maxskilllevel = models.IntegerField()
    


class EventParticipants(models.Model):
    class Meta:
        db_table = 'event_participants'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class EventSpectators(models.Model):
    class Meta:
        db_table = 'event_spectators'
        unique_together = (('spectator', 'event'),)

    spectator = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class EventParticipationRequesters(models.Model):
    class Meta:
        db_table = 'event_spectators'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
