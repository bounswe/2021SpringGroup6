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
