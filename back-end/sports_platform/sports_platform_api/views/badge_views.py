from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Badge


@api_view(['GET'])
def get_badges(request):
    
    badges = Badge.get_badges()
    if badges == 500:
        return Response(data={"message": 'Try later.'}, status=500)

    res = {"badges": badges}
    return Response(data=res, status=200)
