from rest_framework.decorators import api_view
from rest_framework.response import Response
from sports_platform_api.models.event_models import Event

from ..helpers.activity_stream_creation import create_activity_response
from ..models import ActivityStream, Follow, SportSkillLevel
from django.db.models import Q

@api_view(['GET'])
def get_activity_stream(request):
    if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                        status=401)

    limit = int(request.GET.get('limit',-1))
    if limit == -1:
        return Response(data={"message": "Limit must be specified"}, status=400)
    followings = Follow.objects.filter(follower=request.user)
    user_list = [follow.following.user_id for follow in followings]
    
    sport_skill = SportSkillLevel.objects.filter(user=request.user)
    sports = [user_skill.sport.name for user_skill in sport_skill]
    related_events = Event.objects.filter(sport__in=sports)
    event_ids = [event.event_id for event in related_events]

    or_filter = (Q(actor=request.user) | Q(object=request.user) | Q(target__in=event_ids))
        
    offset = int(request.GET.get('offset',0))
    if offset != 0:
        or_filter |= Q(id__lte=offset)        
    
    activities = ActivityStream.objects.filter(or_filter).order_by('-date')[:limit]
    
    response = create_activity_response(activities)
    return Response(response, status=200)