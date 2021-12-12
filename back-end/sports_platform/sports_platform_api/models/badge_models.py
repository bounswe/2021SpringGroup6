from django.db import models
from ..models import User, Event


class Badge(models.Model):
    class Meta:
        db_table = 'badge'

    name = models.CharField(primary_key=True, max_length=30)
    wikidata = models.CharField(max_length=30, blank=True)

    @staticmethod
    def get_badges():
        try:
            badges = Badge.objects.all()

            badges_res = []
            for badge in badges:
                item = {}
                if badge.wikidata:
                    item['@context'] = "https://www.wikidata.org/entity" + badge.wikidata
                    item['name'] = badge.name
                else:
                    item['name'] = badge.name
                
                badges_res.append(item)
            
            return badges_res
        except Exception as e:
            print(e)
            return 500

class UserBadges(models.Model):
    class Meta:
        db_table = 'user_badges'

    user = models.ForeignKey('User', related_name='event_badges', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='user_badges', on_delete=models.CASCADE)
    badge = models.ForeignKey('Badge', related_name='given_badges', on_delete=models.CASCADE)
    


