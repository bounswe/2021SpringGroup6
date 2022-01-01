from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..validation import badge_validation

from ..models import Badge, NewBadgeRequests


@api_view(['GET', 'POST'])
def get_badges(request):
    
    if request.method == 'GET':
        badges = Badge.get_badges()
        if badges == 500:
            return Response(data={"message": 'Try later.'}, status=500)

        res = {"badges": badges}
        return Response(data=res, status=200)

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = badge_validation.NewBadge(data=request.data)
        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)


        validated_body = validation.validated_data
        try:
            res = NewBadgeRequests.create_new_request(validated_body, user)

            if res==500:
                return Response(data={"message": 'Try Later.'}, status=500)
            elif res==400:
                return Response(data={"message": 'Enter a valid sport.'}, status=400)
            else:
                return Response( status=201)
        except Exception as e:
            return Response(data={"message": 'Try Later.'}, status=500)
