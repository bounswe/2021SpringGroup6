from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Sport

@api_view(['GET'])
def get_sports(request):    
    if not request.user.is_authenticated:
        return Response(data={'message': 'User is not logged in, first you need to login'}, status=401)
    
    try:
        sports = Sport.objects.all()
    except Exception:
        return Response(data = {"message": 'There is an internal error, try again later.'}, status=500)
    
    serialized_sports = [sport.name for sport in sports]
    return Response(data = {'sport_names':serialized_sports}, status=200)