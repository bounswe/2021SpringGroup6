from django.db import models
import datetime
from requests.api import get
from ..helpers import get_address
from django.db import transaction
from ..models import Sport
from datetime import datetime, timezone


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

    @staticmethod
    def create_event(data):

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        data['created_on'] = dt
        address = get_address(data['latitude'], data['longitude'])

        if address == 500:
            return 500
        elif address == 400:
            return 101

        data['country'] = address['country']
        data['city'] = address['state']
        data['district'] = address['county']

        try:
            data['sport'] = Sport.objects.get(name=data['sport'])
        except Sport.DoesNotExist:
            return 102
        try:
            with transaction.atomic():
                event = Event.objects.create(**data)
            return {"@id": event.event_id}
        except Exception as e:
            return 500
    
    def _scheme_location(self):
        return {
            '@context': 'https://schema.org',
            '@type': 'Place',
            'geo': {
                '@type':'GeoCoordinates',
                'latitude': float(self.latitude),
                'longitude': float(self.longitude)
            },
            'address': f'{self.district}, {self.city}, {self.country}'
        }
    
    def _scheme_participants(self, participants):
        return [{"@context":"https://schema.org","@type":"Person","@id": participant.user} for participant in participants]

    def _scheme_additional(self, spectators):
        return [
            {
             "@type": "PropertyValue",
             "name": "minimumAttendeeCapacity",
             "value": self.minimumAttendeeCapacity
             },{
            "@type": "PropertyValue",
            "name": "maxSpectatorCapacity",
            "value": self.maxSpectatorCapacity
             },{
            "@type":"PropertyValue",
            "name":"spectator",
            "value":[{"@context":"https://schema.org","@type":"Person","@id": spectator.user} for spectator in spectators]
            }
        ]


    def get_info(self):
        serialized = {}
        serialized['@context'] = 'https://schema.org'
        serialized['@type'] = 'SportsEvent'
        serialized['location'] = self._scheme_location()
        serialized['organizer'] = {'@context':'https://schema.org', '@type':'Person', '@id':self.organizer.user_id}
        participants = EventParticipants.objects.filter(event=self.event_id)
        serialized['attendee'] = self._scheme_participants(participants)
        spectators = EventSpectators.objects.filter(event=self.event_id)
        serialized['additionalProperty'] = self._scheme_additional(spectators)

        return serialized


class EventParticipationRequesters(models.Model):
    class Meta:
        db_table = 'event_participation_requesters'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
