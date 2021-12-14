from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..helpers.activity_stream_creation import create_activity_response
from ..models import ActivityStream

@api_view(['GET'])
def get_activity_stream(request):
    if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                        status=401)

    limit = int(request.GET.get('limit',-1))
    if limit == -1:
        return Response(data={"message": "Limit must be specified"}, status=400)
        
    offset = int(request.GET.get('offset',0))
    if offset == 0:
        activities = ActivityStream.objects.order_by('-date')[:limit]
    else:
        activities = ActivityStream.objects.filter(id__lte=offset).order_by('-date')[:limit]
    
    response = create_activity_response(activities)
    return Response(response, status=200)