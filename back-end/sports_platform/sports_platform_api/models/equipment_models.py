from django.db import models, IntegrityError, transaction
from requests.api import get
from ..helpers import get_address
from django.db import IntegrityError, transaction
from django.db.models import Q
from ..models.activity_stream_models import ActivityStream
from ..models import Sport, User, SportSkillLevel
from datetime import datetime, timezone
from .badge_models import Badge, UserBadges, EventBadges


class EquipmentDiscussionPost(models.Model):
    class Meta:
        db_table = 'equipment_discussion_post'

    post_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        'User', related_name='equipment_posts', on_delete=models.CASCADE)
    sharedContent = models.TextField()
    equipment = models.ForeignKey(
        'Equipment', related_name='equipment_posts', on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField()

    @staticmethod
    def create_post(post_data, user, equipment_id):

        try:
            equipment = Equipment.objects.get(equipment_id=equipment_id)
        except Equipment.DoesNotExist:
            return 402

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:

            if "sharedContent" in post_data.keys():
                obj = EquipmentDiscussionPost.objects.create(
                    equipment=equipment, author=user, dateCreated=dt, text=post_data['text'], sharedContent=post_data['sharedContent'])
            else:
                obj = EquipmentDiscussionPost.objects.create(
                    equipment=equipment, author=user, dateCreated=dt, text=post_data['text'])

            post_dict = dict()
            post_dict["@context"] = "https://schema.org/SocialMediaPosting"
            post_dict["@id"] = obj.post_id
            return post_dict
        except Exception as e:
            return 500

    def comment_post(self, comment_data, user):


        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:

            EquipmentDiscussionComment.objects.create(
                post=self, author=user, text=comment_data['text'], dateCreated=dt)
            return 201
        except:
            return 500


class EquipmentDiscussionComment(models.Model):
    class Meta:
        db_table = 'equipment_comment'

    comment_id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(
        'EquipmentDiscussionPost', related_name='equipment_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        'User', related_name='equipment_comments', on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField()

class Equipment(models.Model):
    class Meta:
        db_table = 'equipment'

    equipment_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    sharedContent = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    created_on = models.DateTimeField()

    @staticmethod
    def create_equipment(data, user):
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        data['created_on'] = dt
        data['creator'] = user
        
        try:
            data['sport'] = Sport.objects.get(name=data['sport'])
        except Sport.DoesNotExist:
            return 102
        try:

            with transaction.atomic():
                equipment = Equipment.objects.create(**data)
            #ActivityStream.objects.create(type='Create', actor=data['organizer'], target=equipment, date=dt)
            # https://schema.org/Product
            return {"@id": equipment.equipment_id}
        except Exception as e:
            return 500

    @staticmethod
    def _create_filter_dict(data):
        filters = {}
        if 'creator' in data:
            filters['creator'] = data['creator']

        if 'nameContains' in data:
            filters['name__contains'] = data['nameContains']

        if 'latitudeBetweenStart' in data:
            filters['latitude__range'] = (
                data['latitudeBetweenStart'], data['latitudeBetweenEnd'])
        if 'longitudeBetweenStart' in data:
            filters['longitude__range'] = (
                data['longitudeBetweenStart'], data['longitudeBetweenEnd'])
        if 'sport' in data:
            filters['sport'] = data['sport']

        return filters

    def get_equipment(self):

        data_dict = dict()

        data_dict['@context'] = "https://schema.org/Product"
        data_dict['@id'] = self.equipment_id
        data_dict['sport'] = {"@type": "Thing", "name": self.sport.name }
        data_dict['geo']= {
            '@type': 'GeoCoordinates',
            'latitude': float(self.latitude),
            'longitude': float(self.longitude)
        }
        data_dict['description'] = self.description
        data_dict['additionalProperty'] = [{
                "@type": "PropertyValue",
                "name": "created_on",
                "value": self.created_on
            }]

        if self.sharedContent:
            data_dict['additionalProperty'].append({
                "@type": "PropertyValue",
                "name": "sharedContent",
                "value": self.sharedContent
            })
            
        data_dict['creator'] = {
            "@type": "Person", 
            "@id": self.creator.user_id, 
            "identifier": self.creator.identifier
        }

        return data_dict

    @staticmethod
    def search(filter):

        filter_dict = Equipment._create_filter_dict(filter)

        try:
            results = Equipment.objects.filter(**filter_dict).order_by('-created_on')

            result_dict = {
                "@context": "https://www.w3.org/ns/activitystreams",
                "type": "OrderedCollection",
                "total_items": len(results)
            }

            result_eq = []

            for res in results:
                result_eq.append(res.get_equipment())

            result_dict['items'] = result_eq

            return result_dict
        except:
            return 500

    def get_posts(self):

        try:
            data = dict()

            posts = self.equipment_posts.all().order_by('dateCreated')

            posts_list = []

            for post in posts:

                post_dict = dict()
                post_dict["@context"] = "https://schema.org/SocialMediaPosting"
                post_dict["@id"] = post.post_id
                if post.sharedContent:
                    post_dict["sharedContent"] = post.sharedContent
                post_dict["author"] = {
                    "@context": "https://schema.org/Person",
                    "@id": post.author.user_id,
                    "identifier": post.author.identifier
                }
                post_dict["text"] = post.text
                post_dict["dateCreated"] = post.dateCreated
                comments = post.equipment_comments.all().order_by('dateCreated')

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

            data["@context"] = "https://schema.org/Product"
            data["@id"] = self.equipment_id
            data["additionalProperty"] = {
                "@type": "PropertyValue",
                "name": "posts",
                "value": posts_list
            }

            return data
        except Exception as e:
            return 500
