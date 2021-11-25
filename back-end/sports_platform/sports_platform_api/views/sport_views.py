from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Sport

@api_view(['GET'])
def get_sports(request):    
    try:
        sports = Sport.objects.all()
    except Exception:
        return Response(data = {"message": 'There is an internal error, try again later.'}, status=500)
    
    serialized_sports = [{"@type":"Thing","name": sport.name,} for sport in sports]
    return Response(data = serialized_sports, status=200)