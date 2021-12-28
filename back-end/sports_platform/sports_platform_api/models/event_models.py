from django.db import models, IntegrityError, transaction
from requests.api import get
from ..helpers import get_address
from django.db import IntegrityError, transaction
from django.db.models import Q
from ..models.activity_stream_models import ActivityStream
from ..models import Sport, User, SportSkillLevel
from datetime import datetime, timezone
from .badge_models import Badge, UserBadges, EventBadges
from ..models.user_models import Notification

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
    message = models.TextField(blank=True)
    requested_on = models.DateTimeField()


class DiscussionPost(models.Model):
    class Meta:
        db_table = 'discussion_post'

    post_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)
    sharedContent = models.TextField()
    event = models.ForeignKey('Event', related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField()

    @staticmethod
    def create_post(post_data, user, event_id):

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            return 402

        if not event.canEveryonePostPosts:
            try:
                EventParticipants.objects.get(event=event, user=user)
            except EventParticipants.DoesNotExist:
                try:
                    EventSpectators.objects.get(event=event, user=user)
                except EventSpectators.DoesNotExist:
                    if user.user_id != event.organizer.user_id:
                        return 401

                except Exception as e:
                    return 500
            except Exception as e:
                return 500

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:

            if "sharedContent" in post_data.keys():
                obj = DiscussionPost.objects.create(
                    event=event, author=user, dateCreated=dt, text=post_data['text'], sharedContent=post_data['sharedContent'])
            else:
                obj = DiscussionPost.objects.create(
                    event=event, author=user, dateCreated=dt, text=post_data['text'])

            post_dict = dict()
            post_dict["@context"] = "https://schema.org/SocialMediaPosting"
            post_dict["@id"] = obj.post_id
            return post_dict
        except Exception as e:
            return 500

    def comment_post(self, comment_data, user):

        if not self.event.canEveryonePostPosts:
            try:
                EventParticipants.objects.get(event=self.event, user=user)
            except EventParticipants.DoesNotExist:
                try:
                    EventSpectators.objects.get(event=self.event, user=user)
                except EventSpectators.DoesNotExist:
                    if user.user_id != self.event.organizer.user_id:
                        return 401

                except:
                    return 500
            except:
                return 500

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:

            DiscussionComment.objects.create(
                post=self, author=user, text=comment_data['text'], dateCreated=dt)

            return 201
        except:
            return 500
class DiscussionComment(models.Model):
    class Meta:
        db_table = 'comment'

    comment_id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey('DiscussionPost', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField()
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
    # if false, only participants and spectators can see
    canEveryoneSeePosts = models.BooleanField(default=True)
    # if false, only participants and spectators can post
    canEveryonePostPosts = models.BooleanField(default=True)
    duration = models.IntegerField()

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

        order = ["state", "province", 
                 "district", "county", "municipality", "city", "town", "village", "hamlet"]

        data['country'] = address['country']

        i = 0
        c = 0

        while i<len(order):
            if order[i] not in address.keys():
                i+=1
                continue
            if c==0:
                data['city'] = address[order[i]]
                i+=1
                c+=1
            else:
                data['district'] = address[order[i]]
                c+=1
                break
        
        if c<1:
            data['city'] = ""
        if c<2:
            data['district'] = ""

        try:
            data['sport'] = Sport.objects.get(name=data['sport'])
        except Sport.DoesNotExist:
            return 102
        try:
            with transaction.atomic():
                event = Event.objects.create(**data)
            ActivityStream.objects.create(type='Create',actor=data['organizer'], target=event, date=dt)
            return {"@id": event.event_id}
        except Exception as e:
            return 500

    @staticmethod
    def search_event(data):
        filter_dict = Event._create_filter_dict(data)
        if 'skillLevel' in data:
            or_filter = Q()
            for skill in data['skillLevel']:
                or_filter |= Q(**{'minSkillLevel__lte':skill, 'maxSkillLevel__gte':skill })
            results = Event.objects.filter(or_filter, **filter_dict).order_by('-startDate')
        else:
            results = Event.objects.filter(**filter_dict).order_by('-startDate')
        return results

    
    @staticmethod
    def _create_filter_dict(data):
        filters = {}
        if 'creator' in data:
            filters['organizer'] = data['creator']
        
        if 'nameContains' in data:
            filters['name__contains'] = data['nameContains']
        
        if ('timeBetweenStart' in data) and ('timeBetweenEnd' in data):
            filters['startDate__time__range'] = (data['timeBetweenStart'],data['timeBetweenEnd'])
        elif 'timeBetweenStart' in data:
            filters['startDate__date'] = data['timeBetweenStart']
        elif 'timeBetweenEnd' in data:
            filters['startDate__date'] = data['timeBetweenEnd']
        
        if ('dateBetweenStart' in data) and ('dateBetweenEnd' in data):
            filters['startDate__date__range'] = (data['dateBetweenStart'],data['dateBetweenEnd'])
        elif 'dateBetweenStart' in data:
            filters['startDate__date'] = data['dateBetweenStart']
        elif 'dateBetweenEnd' in data:
            filters['startDate__date'] = data['dateBetweenEnd']
        
        if 'latitudeBetweenStart' in data:
            filters['latitude__range'] = (data['latitudeBetweenStart'], data['latitudeBetweenEnd'])
        if 'longitudeBetweenStart' in data:
            filters['longitude__range'] = (data['longitudeBetweenStart'], data['longitudeBetweenEnd'])
        
        if 'city' in data:
            filters['city'] = data['city']
        if 'district' in data:
            filters['district'] = data['district']
        if 'country' in data:
            filters['country'] = data['country']
        if 'sport' in data:
            filters['sport'] = data['sport']
        
        return filters

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
        return [{"@context":"https://schema.org","@type":"Person","@id": participant.user.user_id, "identifier": participant.user.identifier} for participant in participants]

    def _scheme_additional(self,interesteds):
        return [
            {
             "@type": "PropertyValue",
             "name": "minimumAttendeeCapacity",
             "value": self.minimumAttendeeCapacity
             },{
            "@type": "PropertyValue",
            "name": "maxSpectatorCapacity",
            "value": self.maxSpectatorCapacity
             },
             {
            "@type": "PropertyValue",
            "name": "interesteds",
            "value": [{"@context":"https://schema.org","@type":"Person","@id": interested.user.user_id, "identifier": interested.user.identifier} for interested in interesteds]
             },
             {
            "@type": "PropertyValue",
            "name": "acceptWithoutApproval",
            "value": self.acceptWithoutApproval
             }
        ]

    def get_info(self):
        serialized = {}
        serialized['@context'] = 'https://schema.org'
        serialized['@type'] = 'SportsEvent'
        serialized['location'] = self._scheme_location()
        serialized['organizer'] = {'@context':'https://schema.org', '@type':'Person', '@id':self.organizer.user_id, "identifier":self.organizer.identifier}
        participants = EventParticipants.objects.filter(event=self.event_id)
        serialized['attendee'] = self._scheme_participants(participants)
        spectators = EventSpectators.objects.filter(event=self.event_id)
        serialized['audience'] = [{"@context":"https://schema.org","@type":"Person","@id": spectator.user.user_id, "identifier":spectator.user.identifier} for spectator in spectators]
        interesteds = EventSpectators.objects.filter(event=self.event_id)
        serialized['additionalProperty'] = self._scheme_additional(interesteds)

        return serialized

    def add_interest(self, user_id, message):

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:
            requester = User.objects.get(user_id=user_id)

            try:
                EventSpectators.objects.get(event=self, user=requester)
                return 405  # already participating
            except EventSpectators.DoesNotExist:
                pass
            
            try:
                EventParticipants.objects.get(event=self, user=requester)
                return 404  # already participating
            except EventParticipants.DoesNotExist:
                pass

            try:
                user_skill_level = SportSkillLevel.objects.get(user=requester, sport=self.sport).skill_level
                if user_skill_level < self.minSkillLevel or user_skill_level > self.maxSkillLevel:
                    return 407

            except SportSkillLevel.DoesNotExist:
                return 406

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

            if interested.message:
                data_dict['additionalProperty'] = {
                    "@type": "PropertyValue",
                    "name": f"MessageToParticipateEvent{interested.event.event_id}",
                    "value": interested.message
                }

            interested_users.append(data_dict)

        return interested_users

    def add_participant(self, accept_user_id_list, reject_user_id_list):

        if self.acceptWithoutApproval:
            return 401

        num_remaining_places = self.maximumAttendeeCapacity - \
            len(self.participant_users.all())
        
        data_dict = dict()
        data_dict['@context'] = "https://www.w3.org/ns/activitystreams"
        data_dict['summary'] = f"{self.organizer.identifier} accepted and rejected users to '{self.name}' event"
        data_dict['type'] = "Collection"

        data_dict['items'] = []

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        limit_for_notification = int(self.maximumAttendeeCapacity*0.1)
        if num_remaining_places in [limit_for_notification, limit_for_notification+1, limit_for_notification-1]:
            interesteds = self.interested_users.all()
            for interested in interesteds:
                Notification.objects.create(event_id=self, user_id=interested.user, date=dt,notification_type=f'{num_remaining_places} Spots Left')

        try:
            with transaction.atomic():
                for user in accept_user_id_list:
                    if num_remaining_places <= 0:
                        participants = self.participant_users.all()
                        for participant in participants:
                            Notification.objects.create(event_id=self, user_id=participant.user, date=dt,notification_type=f'Event Full')

                        break

                    try:
                        request_object = EventParticipationRequesters.objects.get(event=self, user=user)
                    except:
                        continue

                    try:
                        EventParticipants.objects.get(event=self, user=user)
                        continue  # already participating
                    except EventParticipants.DoesNotExist:
                        pass

                    try:
                        EventSpectators.objects.get(event=self, user=user)
                        continue  # already a spectator
                    except EventSpectators.DoesNotExist:
                        pass

                    EventParticipants.objects.create(
                        event=self, user=request_object.user, accepted_on=dt)
                    ActivityStream.objects.create(type='Accept', actor=self.organizer, target=self, object=request_object.user, date=dt)
                    Notification.objects.create(event_id=self, user_id=request_object.user, date=dt,notification_type='Event Acceptance')
                    request_object.delete()

                    acception = dict()
                    acception['@context'] = "https://www.w3.org/ns/activitystreams"
                    acception['summary'] = f"{self.organizer.identifier} accepted {request_object.user.identifier} to event '{self.name}'."
                    acception['type'] = "Accept"

                    acception['actor'] = {
                        "type": "https://schema.org/Person",
                        "@id":  self.organizer.user_id,
                        "identifier": self.organizer.identifier
                    }

                    acception['object'] = {
                        "type": "RequestToParticipate",
                        "actor": {
                            "type": "https://schema.org/Person",
                            "@id":  request_object.user.user_id,
                            "identifier": request_object.user.identifier
                        },
                        "object": {
                            "type": "https://schema.org/SportsEvent",
                            "@id":  self.event_id,
                        }
                    }

                    if request_object.message:
                        acception['object']['attachment'] = {
                            "type": "Note",
                            "content": request_object.message
                        }

                    num_remaining_places -= 1
                    data_dict['items'].append(acception)

                for user in reject_user_id_list:

                    try:
                        request_object = EventParticipationRequesters.objects.get(event=self, user=user)
                    except:
                        continue

                    try:
                        EventParticipants.objects.get(event=self, user=user)
                        continue  # already participating
                    except EventParticipants.DoesNotExist:
                        pass

                    try:
                        EventSpectators.objects.get(event=self, user=user)
                        continue  # already a spectator
                    except EventSpectators.DoesNotExist:
                        pass
                    Notification.objects.create(event_id=self, user_id=request_object.user, date=dt,notification_type='Event Rejection')
                    request_object.delete()
                    rejected = dict()
                    rejected['@context'] = "https://www.w3.org/ns/activitystreams"
                    rejected['summary'] = f"{self.organizer.identifier} rejected {request_object.user.identifier}'s request to join the event '{self.name}'."
                    rejected['type'] = "Reject"

                    rejected['actor'] = {
                        "type": "https://schema.org/Person",
                        "@id":  self.organizer.user_id,
                        "identifier": self.organizer.identifier
                    }

                    rejected['object'] = {
                        "type": "RequestToParticipate",
                        "actor": {
                            "type": "https://schema.org/Person",
                            "@id":  request_object.user.user_id,
                            "identifier": request_object.user.identifier
                        },
                        "object": {
                            "type": "https://schema.org/SportsEvent",
                            "@id":  self.event_id,
                        }
                    }

                    data_dict['items'].append(rejected)
        except Exception as e:
            return 500

        data_dict['total_items'] = len(data_dict['items'])
        return data_dict

    def get_participants(self):

        try:
            participating = self.participant_users.all()
        except Exception as e:
            return 500

        participant_users = []

        for participant in participating:

            data_dict = dict()

            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = participant.user.user_id
            data_dict['identifier'] = participant.user.identifier

            participant_users.append(data_dict)

        return participant_users

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

    def delete_participant(self, user):

        try:
            request_object = EventParticipants.objects.get(event=self, user=user)
            request_object.delete()
            return True
        except EventParticipants.DoesNotExist:
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
                return 404  # already participating
            except EventParticipants.DoesNotExist:
                pass

            try:
                EventParticipationRequesters.objects.get(event=self, user=requester)
                return 405  # already participating
            except EventParticipationRequesters.DoesNotExist:
                pass

            EventSpectators.objects.create(
                event=self, user=requester, requested_on=dt)
            ActivityStream.objects.create(type='Spectator', actor=requester, target=self, date=dt)

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
        
    def get_badges(self):

        data = dict()

        try:
            event_badges = self.event_badges.all()

            badges_list = []

            for badge in event_badges:
                item = dict()
                if badge.badge.wikidata:
                    item['@context'] = "https://www.wikidata.org/entity/" + badge.badge.wikidata
                    item['name'] = badge.badge.name
                else:
                    item['name'] = badge.badge.name

                badges_list.append(item)


            data["@context"] = "https://schema.org/SportsEvent"
            data["@id"] = self.event_id
            data["additionalProperty"] = {
                    "@type": "PropertyValue",
                    "name": "event_badges",
                    "value": badges_list
                }
        

            return data
        except Exception as e:
            return 500

    def add_badge(self, badge):

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        try:
            badge = Badge.objects.get(name=badge)
            EventBadges.objects.create(event=self, badge=badge, date=dt)

        except Badge.DoesNotExist:
            return 401
        except IntegrityError:
            return 402
        except:
            return 500


    def get_posts(self, user):

        if not self.canEveryoneSeePosts:
            try:
                EventParticipants.objects.get(event=self, user=user)
            except EventParticipants.DoesNotExist:
                try:
                    EventSpectators.objects.get(event=self, user=user)
                except EventSpectators.DoesNotExist:
                    if user.user_id != self.organizer.user_id:
                        return 401
                except Exception as e:
                    return 500
            except Exception as e:
                return 500

        try:
            data = dict()

            posts = self.posts.all().order_by('dateCreated')

            posts_list = []

            for post in posts:

                post_dict = dict()
                post_dict["@context"] = "https://schema.org/SocialMediaPosting"
                post_dict["@id"] = post.post_id
                if post.sharedContent:
                    post_dict["sharedContent"] = post.sharedContent
                post_dict["author"] = {
                    "@context" : "https://schema.org/Person",
                    "@id" : post.author.user_id,
                    "identifier": post.author.identifier
                }
                post_dict["text"] = post.text
                post_dict["dateCreated"] = post.dateCreated
                comments = post.comments.all().order_by('dateCreated')

                comment_list = []
                for comment in comments:
                    comment_dict = dict()
                    comment_dict["@context"] = "https://schema.org/Comment"
                    comment_dict["@id"] = comment.comment_id
                    comment_dict["author"] = {
                        "@context": "https://schema.org/Person",
                        "@id": comment.author.user_id,
                        "identifier": comment.author.identifier
                    }
                    comment_dict["text"] = comment.text
                    comment_dict["dateCreated"] = comment.dateCreated
                    comment_list.append(comment_dict)

                post_dict["comment"] = comment_list
                posts_list.append(post_dict)

            data["@context"] = "https://schema.org/SportsEvent"
            data["@id"] = self.event_id
            data["additionalProperty"] = {
                "@type": "PropertyValue",
                "name": "posts",
                "value": posts_list
            }

            return data
        except Exception as e:
            return 500


    def update(self, data):
        participants = EventParticipants.objects.filter(event=self)
        if 'maximumAttendeeCapacity' in data:
            if len(participants) > data['maximumAttendeeCapacity']:
                return 400 # there are more participants already
        if 'minSkillLevel' in data:
            for participant in participants:
                try:
                    user_skill_level = SportSkillLevel.objects.get(user=participant.user,sport=self.sport)
                    if user_skill_level.skill_level < data['minSkillLevel']:
                        return 401 # there is a participant with lower skill
                except SportSkillLevel.DoesNotExist:
                    pass
        if 'maxSkillLevel' in data:
            for participant in participants:
                try:
                    user_skill_level = SportSkillLevel.objects.get(user=participant.user,sport=self.sport)
                    if user_skill_level.skill_level > data['maxSkillLevel']:
                        return 402 # there is a participant with higher skill
                except SportSkillLevel.DoesNotExist:
                    pass
        if 'maxSpectatorCapacity' in data:
            spectators = EventSpectators.objects.filter(event=self)
            if len(spectators) > data['maxSpectatorCapacity']:
                return 403 # there are more spectators already
        Event.objects.filter(pk=self.event_id).update(**data)
        participants = self.participant_users.all()
        utc_dt = datetime.now(timezone.utc)
        dt = utc_dt.astimezone()
        for participant in participants:
            Notification.objects.create(event_id=self, user_id=participant.user, date=dt,notification_type=f'Event Update')
        return 200
