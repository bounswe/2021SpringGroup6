from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import datetime
from django.db import IntegrityError

from .activity_stream_models import ActivityStream
from .badge_models import Badge, UserBadges
from ..helpers.notification_creation import prepare_notifications

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, identifier, email, password, **extra_fields):
        """
        Create and save a user with the given identifer, email, and password.
        """
        if not identifier:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        identifier = GlobalUserModel.normalize_username(identifier)
        user = self.model(identifier=identifier, email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, identifier, email, password, **extra_fields):
        return self._create_user(identifier, email, password, **extra_fields)

    def create_superuser(self, identifier, email, password, **extra_fields):
        return self._create_user(identifier, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class Notification(models.Model):
    class Meta:
        db_table = 'notifications'
        unique_together = (('event_id','user_id','notification_type'))
    
    event_id = models.ForeignKey('Event', related_name='not_event', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    notification_type = models.CharField(max_length=50,null=False)
    user_id = models.ForeignKey('User', related_name='receiver', on_delete=models.CASCADE)
    read =  models.BooleanField(default=False)


class Follow(models.Model):
    class Meta:
        db_table = 'follow'
        unique_together = (('follower', 'following'),)

    follower = models.ForeignKey('User', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('User', related_name='follower', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

class Block(models.Model):
    class Meta:
        db_table = 'block'
        unique_together = (('blocker', 'blocked'),)
        
    blocker = models.ForeignKey('User', related_name='+', on_delete=models.CASCADE)
    blocked = models.ForeignKey('User', related_name='+', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

class User(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    email_visibility = models.BooleanField(default=True)
    password = models.CharField(max_length=300)
    identifier = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=300,blank=True)
    name_visibility = models.BooleanField(default=True)
    familyName = models.CharField(max_length=30,blank=True)
    familyName_visibility = models.BooleanField(default=True)
    birthDate = models.DateField(blank=True, null=True)
    birthDate_visibility = models.BooleanField(default=True)
    gender = models.CharField(max_length=40,blank=True, null=True)
    gender_visibility = models.BooleanField(default=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location_visibility = models.BooleanField(default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['email']

    def block(self, user_id):
        date = datetime.datetime.now()
        try:
            user_to_block = User.objects.get(user_id=user_id)
            Block.objects.create(blocker = self, blocked = user_to_block, date = date)
            ActivityStream.objects.create(type='Block',actor=self, object=user_to_block, date=date)
            return True
        except User.DoesNotExist:
            return 401
        except IntegrityError:
            return 402
        except Exception:
            return 500

    def set_visibility(self, info):
        User.objects.filter(pk=self.user_id).update(**info)

    def follow(self, user_id):
        date = datetime.datetime.now()
        try:
            to_follow = User.objects.get(user_id=user_id)
            Follow.objects.create(follower = self, following = to_follow, date = date)
            ActivityStream.objects.create(type='Follow',actor=self, object=to_follow, date=date)
            return True
        except User.DoesNotExist:
            return 401
        except IntegrityError as e:
            return 402
        except Exception as e:
            return 500

    def unfollow(self, user_id):
        try:
            num_deleted, _ = Follow.objects.filter(follower = self.user_id, following = user_id).delete()
            if num_deleted == 0:
                return 403
        except Exception as e:
            return 500
        
    def unblock(self, user_id):
        try:
            num_unblocked, _ = Block.objects.filter(blocker=self.user_id, blocked=user_id).delete()
            if num_unblocked == 0:
                return 403
        except Exception:
            return 500

    def add_sport_interest(self, sport_name, skill_level):
        SportSkillLevel.objects.create(user_id=self.user_id,sport_id=sport_name, skill_level=skill_level)
    
    def get_sport_skills(self):
        skills = SportSkillLevel.objects.filter(user=self.user_id)
        return [{"@type":"PropertyValue","name": skill.sport_id, "value":skill.skill_level} for skill in skills]
    
    def update(self, sport_data, update_info):
        User.objects.filter(pk=self.user_id).update(**update_info)
        if sport_data:
            for skills in sport_data:
                sport_skill = SportSkillLevel.objects.filter(user_id=self.user_id, sport_id=skills['sport'])
                if len(sport_skill) == 0:# adding new sport skill
                    self.add_sport_interest(skills['sport'], skills['skill_level'])
                else:# updating the skill level
                    sport_skill.update(**skills)

    def delete(self):
        User.objects.filter(pk=self.user_id).delete()

    def get_following(self):
        try:
            following = self.following.all()

            data_dict = dict()
            data_dict['@context'] = "https://www.w3.org/ns/activitystreams"
            data_dict['summary'] = f"{self.identifier}'s following activities."
            data_dict['type'] = "Collection"
            data_dict['total_items'] = len(following)
            data_dict['items'] = []

            for following_user in following:
                one_follow = dict()
                one_follow['@context'] = "https://www.w3.org/ns/activitystreams"
                one_follow['summary'] = f"{self.identifier} followed {following_user.following.identifier}"
                one_follow['type'] = "Follow"

                one_follow['actor'] = {
                    "type": "https://schema.org/Person",
                    "@id":  self.user_id,
                    "identifier": self.identifier
                }

                one_follow['object'] = {
                    "type": "https://schema.org/Person",
                    "@id":  following_user.following.user_id,
                    "identifier": following_user.following.identifier
                }

                data_dict['items'].append(one_follow)

            return data_dict
        except Exception as e:
            return 500

    def get_follower(self):
        try:
            follower = self.follower.all()

            data_dict = dict()
            data_dict['@context'] = "https://www.w3.org/ns/activitystreams"
            data_dict['summary'] = f"{self.identifier}'s being followed activities."
            data_dict['type'] = "Collection"
            data_dict['total_items'] = len(follower)
            data_dict['items'] = []

            for follower_user in follower:
                one_follow = dict()
                one_follow['@context'] = "https://www.w3.org/ns/activitystreams"
                one_follow['summary'] = f"{follower_user.follower.identifier} followed {self.identifier}"
                one_follow['type'] = "Follow"

                one_follow['actor'] = {
                    "type": "https://schema.org/Person",
                    "@id":  follower_user.follower.user_id,
                    "identifier": follower_user.follower.identifier
                }

                one_follow['object'] = {
                    "type": "https://schema.org/Person",
                    "@id":  self.user_id,
                    "identifier": self.identifier
                }

                data_dict['items'].append(one_follow)

            return data_dict
        except Exception as e:
            return 500
    
    def get_blocked(self):
        try:
            blockeds = Block.objects.filter(blocker=self.user_id)

            data_dict = dict()
            data_dict['@context'] = "https://www.w3.org/ns/activitystreams"
            data_dict['summary'] = f"{self.identifier}'s blocking activities."
            data_dict['type'] = "Collection"
            data_dict['total_items'] = len(blockeds)
            data_dict['items'] = []

            for blocked_user in blockeds:
                one_block = dict()
                one_block['@context'] = "https://www.w3.org/ns/activitystreams"
                one_block['summary'] = f"{self.identifier} blocked {blocked_user.blocked.identifier}"
                one_block['type'] = "Block"

                one_block['actor'] = {
                    "type": "https://schema.org/Person",
                    "@id":  self.user_id,
                    "identifier": self.identifier
                }

                one_block['object'] = {
                    "type": "https://schema.org/Person",
                    "@id":  blocked_user.blocked.user_id,
                    "identifier": blocked_user.blocked.identifier
                }

                data_dict['items'].append(one_block)

            return data_dict
        except Exception:
            return 500

    def get_participating_events(self):

        try:
            events = self.participating_events.all().order_by('event_id')

            data_dict = dict()
            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = self.user_id
            data_dict['identifier'] = self.identifier
            data_dict['additionalProperty'] = dict()
            data_dict['additionalProperty'] = {
                "@type": "PropertyValue",
                "name": "participatingEvents",
                "value": []
            }

            for event in events:

                event_dict = {
                    "type": "https://schema.org/SportsEvent",
                    "@id":  event.event.event_id,
                    "name": event.event.name,
                    "sport": event.event.sport.name,
                    "startDate": event.event.startDate,
                    "location": event.event._scheme_location(),
                    "maximumAttendeeCapacity": event.event.maximumAttendeeCapacity
                }

                data_dict['additionalProperty']['value'].append(event_dict)

            return data_dict
        except Exception as e:
            return 500

    def get_interested_events(self):

        try:
            events = self.interested_events.all().order_by('event_id')

            data_dict = dict()
            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = self.user_id
            data_dict['identifier'] = self.identifier
            data_dict['additionalProperty'] = dict()
            data_dict['additionalProperty'] = {
                "@type": "PropertyValue",
                "name": "interestedEvents",
                "value": []
            }

            for event in events:

                event_dict = {
                    "type": "https://schema.org/SportsEvent",
                    "@id":  event.event.event_id,
                    "name": event.event.name,
                    "sport": event.event.sport.name,
                    "startDate": event.event.startDate,
                    "location": event.event._scheme_location(),
                    "maximumAttendeeCapacity": event.event.maximumAttendeeCapacity
                }

                data_dict['additionalProperty']['value'].append(event_dict)

            return data_dict
        except Exception as e:
            return 500

    def get_spectating_events(self):

        try:
            events = self.spectating_events.all().order_by('event_id')

            data_dict = dict()
            data_dict['@context'] = "https://schema.org/Person"
            data_dict['@id'] = self.user_id
            data_dict['identifier'] = self.identifier
            data_dict['additionalProperty'] = dict()
            data_dict['additionalProperty'] = {
                "@type": "PropertyValue",
                "name": "spectatingEvents",
                "value": []
            }

            for event in events:

                event_dict = {
                    "type": "https://schema.org/SportsEvent",
                    "@id":  event.event.event_id,
                    "name": event.event.name,
                    "sport": event.event.sport.name,
                    "startDate": event.event.startDate,
                    "location": event.event._scheme_location(),
                    "maxSpectatorCapacity": event.event.maxSpectatorCapacity
                }

                data_dict['additionalProperty']['value'].append(event_dict)

            return data_dict
        except Exception as e:
            return 500

    def get_badges(self):
        
        data = dict()

        try:
            user_given_badges = self.badges_by_users.all()

            user_given_badges_list = []

            for badge in user_given_badges:
                item = dict()
                if badge.badge.wikidata:
                    item['@context'] = "https://www.wikidata.org/entity/" + badge.badge.wikidata
                    item['name'] = badge.badge.name
                    item['additionalProperty'] = {
                        "@type": "PropertyValue",
                        "name": "givenBy",
                        "value": {
                            "@context": "https://schema.org/Person",
                            "@id": badge.from_user.user_id
                        }
                    }
                else:
                    item['name'] = badge.badge.name
                    item['additionalProperty'] = {
                        "@type": "PropertyValue",
                        "name": "givenBy",
                        "value": {
                            "@context": "https://schema.org/Person",
                            "@id": badge.from_user.user_id
                        }
                    }

                user_given_badges_list.append(item)

            participating_events = self.participating_events.all()

            utc_dt = datetime.datetime.now(datetime.timezone.utc)  # UTC time
            dt = utc_dt.astimezone()

            event_given_badge_list = []

            for event in participating_events:

                if event.event.startDate > dt:
                    continue
                
                for badge in event.event.event_badges.all():
                    item = dict()
                    if badge.badge.wikidata:
                        item['@context'] = "https://www.wikidata.org/entity/" + badge.badge.wikidata
                        item['name'] = badge.badge.name
                    else:
                        item['name'] = badge.badge.name
                    item['additionalProperty'] = {
                        "@type": "PropertyValue",
                        "name": "event",
                        "value": {
                            "@context": "https://schema.org/SportsEvent",
                            "@id": event.event.event_id
                        }
                    }

                    event_given_badge_list.append(item)

            data["@context"] =  "https://schema.org/Person"
            data["@id"] = self.user_id
            data["additionalProperty"] = [
                {
                    "@type": "PropertyValue",
                    "name": "event_badges",
                    "value": event_given_badge_list
                },
                {
                    "@type": "PropertyValue",
                    "name": "user_badges",
                    "value": user_given_badges_list
                }
            ]

            return data
        except Exception as e:
            return 500

    def give_badge(self, user_id, badge):

        utc_dt = datetime.datetime.now(datetime.timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        try:
            badge = Badge.objects.get(name = badge)
            user = User.objects.get(user_id = user_id)
            UserBadges.objects.create(user = user, from_user = self, badge = badge, date=dt )
            return True
        except Badge.DoesNotExist:
            return 401
        except User.DoesNotExist:
            return 402
        except IntegrityError:
            return 403
        except:
            return 500
    
    @staticmethod
    def search_user(data, block_check, user):
        filter_dict = User._create_filter_dict(data)
        results = User.objects.filter(**filter_dict)
        if not block_check:
            return results
        filtered_results = []
        for user_res in results:
            blocks = Block.objects.filter(blocker=user_res, blocked=user)
            if not blocks.exists():
                filtered_results.append(user_res)
        return filtered_results

    @staticmethod
    def _create_filter_dict(data):
        filters = {}
        if 'name' in data:
            filters['name__contains'] = data['name']
        if 'familyName' in data:
            filters['familyName__contains'] = data['familyName']
        if 'identifier' in data:
            filters['identifier__contains'] = data['identifier']
        
        return filters
        
    def get_notifications(self):
        notifications = Notification.objects.filter(user_id=self, read=False).order_by('date')
        return prepare_notifications(notifications)

class SportSkillLevel(models.Model):
    class Meta:
        db_table = 'sport_skill_level'
        unique_together = (('user', 'sport'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    skill_level = models.SmallIntegerField()