from django.db import models
from .sport_models import Sport
from datetime import datetime, timezone
from .sport_models import Sport

class Badge(models.Model):
    class Meta:
        db_table = 'badge'

    name = models.CharField(primary_key=True, max_length=30)
    wikidata = models.CharField(max_length=30, blank=True)
    sport = models.ForeignKey('Sport', blank=True, on_delete=models.CASCADE)

    @staticmethod
    def get_badges():
        try:
            badges = Badge.objects.all()

            badges_res = []
            for badge in badges:
                item = {}
                item['name'] = badge.name
                if badge.wikidata:
                    item['@context'] = "https://www.wikidata.org/entity/" + badge.wikidata
                if badge.sport:
                    item['sport'] = badge.sport.name
                    
                badges_res.append(item)
            
            return badges_res
        except Exception as e:
            return 500

class UserBadges(models.Model):
    class Meta:
        db_table = 'user_given_badges'
        unique_together = (('user', 'from_user', 'badge'),)

    user = models.ForeignKey('User', related_name='badges_by_users', on_delete=models.CASCADE)
    from_user = models.ForeignKey('User', related_name='gave_badges', on_delete=models.CASCADE)
    badge = models.ForeignKey('Badge', related_name='given_badges_by_users', on_delete=models.CASCADE)
    date = models.DateTimeField()
    
class EventBadges(models.Model):
    class Meta:
        db_table = 'event_badges'
        unique_together = (('event', 'badge'),)

    event = models.ForeignKey('Event', related_name='event_badges', on_delete=models.CASCADE)
    badge = models.ForeignKey('Badge', related_name='given_badges_by_events', on_delete=models.CASCADE)
    date = models.DateTimeField()


class NewBadgeRequests(models.Model):

    class Meta:
        db_table = 'new_badges'

    date = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', blank=True, null=True, on_delete=models.CASCADE)

    @staticmethod
    def create_new_request(data,user):
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        try:

            if "sport" in data.keys():
                sport = Sport.objects.get(name=data['sport'])
                NewBadgeRequests.objects.create(sport=sport, description=data['description'], date=dt, user=user)
                return 201
            else:
                NewBadgeRequests.objects.create(description=data['description'], date=dt, user=user)
                return 201

        except Sport.DoesNotExist:
            return 400
        except Exception as e:
            return 500

