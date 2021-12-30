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