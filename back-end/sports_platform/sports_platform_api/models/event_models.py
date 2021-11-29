from django.db import models
import datetime
from requests.api import get
from ..helpers import get_address
from django.db import IntegrityError, transaction
from ..models import Sport

class Event(models.Model):
    class Meta:
        db_table = 'event'

    event_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    organizer = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    startDate = models.DateTimeField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    minimumAttendeeCapacity = models.IntegerField()
    maximumAttendeeCapacity = models.IntegerField()
    maxSpectatorCapacity = models.IntegerField()
    minSkillLevel = models.IntegerField()
    maxSkillLevel = models.IntegerField()

    created_on = models.DateTimeField()
    


class EventParticipants(models.Model):
    class Meta:
        db_table = 'event_participants'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class EventSpectators(models.Model):
    class Meta:
        db_table = 'event_spectators'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class EventParticipationRequesters(models.Model):
    class Meta:
        db_table = 'event_participation_requesters'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
