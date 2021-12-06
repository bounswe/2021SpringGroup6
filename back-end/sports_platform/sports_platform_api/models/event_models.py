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

    acceptWithoutApproval = models.BooleanField()
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

    def add_interest(self, user_id, message):

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:
            requester = User.objects.get(user_id=user_id)

            try:
                EventParticipants.objects.get(event=self, user=requester)
                return 404  # already patricipating
            except EventParticipants.DoesNotExist:
                pass
            if self.acceptWithoutApproval:
                num_remaining_places = self.maximumAttendeeCapacity - \
                    len(self.participant_users.all())
                if num_remaining_places == 0:
                    return 403  # no place left
                else:
                    EventParticipants.objects.create(
                        event=self, user=requester, accepted_on=dt)
                    return True
            else:
                if "message" in message.keys():
                    EventParticipationRequesters.objects.create(
                        event=self, user=requester, requested_on=dt, message=message['message'])
                else:
                    EventParticipationRequesters.objects.create(
                        event=self, user=requester, requested_on=dt)
                return True
        except User.DoesNotExist:  # User does not exist
            return 401
        except IntegrityError as e:  # already sent request
            return 402
        except Exception as e:
            return 500

    def add_participant(self, user_id_list):
        
        num_remaining_places = self.maximumAttendeeCapacity - len(self.participant_users.all())
    def get_interesteds(self):

        if self.acceptWithoutApproval:
            return 400

        try:
            interesteds = self.interested_users.all()
        except:
            return 500

        interested_users = []

        for interested in interesteds:

            data_dict = dict()

            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = interested.user.user_id
            data_dict['identifier'] = interested.user.identifier

            interested_users.append(data_dict)

        return interested_users

        data_dict = dict()
        data_dict['@context'] = "https://www.w3.org/ns/activitystreams"
        data_dict['summary'] = f"{self.organizer.identifier} accepted users to {self.name} event"
        data_dict['type'] = "Collection"
        
        data_dict['items'] = []

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:
            with transaction.atomic():
                for user in user_id_list:
                    print(user_id_list)
                    if num_remaining_places <= 0:
                        data_dict['total_items'] = len(data_dict['items'])
                        return data_dict

                    try:
                        request_object = EventParticipationRequesters.objects.get(user = user)
                        print(request_object)
                    except:
                        continue

                    EventParticipants.objects.create(event=self, user=request_object.user, accepted_on=dt)
                    request_object.delete()

                    acception = dict()
                    acception['@context'] = "https://www.w3.org/ns/activitystreams"
                    acception['summary'] = f"{self.organizer.name} accepted {request_object.user.identifier} to event {self.name}."
                    acception['type'] = "Accept"

                    acception['actor'] = {
                        "type": "https://schema.org/Person",
                        "@id":  self.organizer.user_id,
                        "identifier": self.organizer.identifier
                    }

                    acception['object'] = {
                        "type": "https://schema.org/Person",
                        "@id":  request_object.user.user_id,
                        "identifier": request_object.user.identifier
                    }

                    acception['target'] = {
                        "type": "https://schema.org/SportsEvent",
                        "@id":  self.event_id,
                    }

                    num_remaining_places -= 1
                    data_dict['items'].append(acception)
        except:
            return 500
                

        data_dict['total_items'] = len(data_dict['items'])
        return data_dict
    def delete_interest(self, user):

        try:
            request_object = EventParticipationRequesters.objects.get(event=self, user=user)
            request_object.delete()
            return True
        except EventParticipationRequesters.DoesNotExist:
            return 401
        except Exception as e:
            return 500

    def delete_spectator(self, user):

        try:
            request_object = EventSpectators.objects.get(event=self, user=user)
            request_object.delete()
            return True
        except EventSpectators.DoesNotExist:
            return 401
        except Exception as e:
            return 500
    def add_spectator(self, user_id):
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        try:
            num_of_spectators = len(self.spectator_users.all())
            if num_of_spectators >= self.maxSpectatorCapacity:
                return 403  # Full Capacity
            requester = User.objects.get(user_id=user_id)

            try:
                EventParticipants.objects.get(event=self, user=requester)
                return 404  # already patricipating
            except EventParticipants.DoesNotExist:
                pass

            try:
                EventParticipationRequesters.objects.get(event=self, user=requester)
                return 405  # already patricipating
            except EventParticipants.DoesNotExist:
                pass

            EventSpectators.objects.create(
                event=self, user=requester, requested_on=dt)
            return True
        except User.DoesNotExist:  # User does not exist
            return 401
        except IntegrityError as e:  # already a spectator
            return 402
        except Exception as e:
            return 500

    def get_spectators(self):

        try:
            spectators = self.spectator_users.all()
        except Exception as e:
            return 500

        spectator_users = []

        for spectator in spectators:

            data_dict = dict()

            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = spectator.user.user_id
            data_dict['identifier'] = spectator.user.identifier

            spectator_users.append(data_dict)

        return spectator_users


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
    message = models.TextField()
    requested_on = models.DateTimeField()
