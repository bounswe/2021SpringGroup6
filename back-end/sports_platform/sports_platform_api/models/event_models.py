from django.db import models
import datetime
from requests.api import get
from ..helpers import get_address
from django.db import IntegrityError, transaction
from ..models import Sport, User
from datetime import datetime, timezone

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


    def add_interest(self, user_id):
        
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        try:
            requester = User.objects.get(user_id=user_id)
            EventParticipationRequesters.objects.create(event=self, user=requester, requested_on = dt)
            return True
        except User.DoesNotExist: # User does not exist
            return 401
        except IntegrityError as e: # already sent request
            return 402 
        except Exception as e:
            return 500

    def add_spectator(self, user_id):
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        try:
            num_of_spectators = len(self.interested_users.all())
            if num_of_spectators >= self.maxSpectatorCapacity:
                return 403 # Full Capacity
            requester = User.objects.get(user_id=user_id)
            EventSpectators.objects.create(event=self, user=requester, requested_on=dt)
            return True
        except User.DoesNotExist:  # User does not exist
            return 401
        except IntegrityError as e:  # already a spectator
            return 402
        except Exception as e:
            return 500


class EventParticipants(models.Model):
    class Meta:
        db_table = 'event_participants'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', related_name='participating_events', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='participant_users', on_delete=models.CASCADE)
    accepted_on = models.DateTimeField()


class EventSpectators(models.Model):
    class Meta:
        db_table = 'event_spectators'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', related_name='spectating_events', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='spectator_users',  on_delete=models.CASCADE)
    requested_on = models.DateTimeField()


class EventParticipationRequesters(models.Model):
    class Meta:
        db_table = 'event_participation_requesters'
        unique_together = (('user', 'event'),)

    user = models.ForeignKey('User', related_name='interested_events', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='interested_users', on_delete=models.CASCADE)
    requested_on = models.DateTimeField()
