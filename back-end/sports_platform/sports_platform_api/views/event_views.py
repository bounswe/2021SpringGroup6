from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Event
from ..validation import event_validation



@api_view(['POST'])
def create_event(request):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    organizer = request.user

    validation = event_validation.Event(data=request.data)

    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    validated_body = validation.validated_data
    validated_body['organizer'] = organizer


    try:
        res = Event.create_event(validated_body)
        
        if res == 101:
            return Response(data={"message": 'Check coordinates.'}, status=400)
        elif res == 102:
            return Response(data={"message": 'Enter a valid sport.'}, status=400)
        elif res == 500:
            return Response(data={"message": 'Try Later.'}, status=500)

        response = dict()
        response['@context'] = 'https://schema.org/SportsEvent'
        response['@id'] = res['@id']

        return Response(data=response, status=201)
        
    except Exception:
        return Response(data={"message": 'There is an internal error, try again later.'}, status=500)


@api_view(['POST'])
def attend_spectator(request, event_id):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    user = request.user

    try:
        event = Event.objects.get(event_id = event_id)

        res = event.add_spectator(user.user_id)

        if res == 401:
            return Response(data={"message": "Try with a valid user."}, status=400)
        elif res == 402:
            return Response(data={"message": "Already a spectator for the event."}, status=400)
        elif res == 403:
            return Response(data={"message": "Spectator capacity is full for this event."}, status=400)
        elif res == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(status=201)

    except Exception:
        return Response(data={"message": 'Try later.'}, status=500)


@api_view(['POST'])
def add_interest(request, event_id):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    user = request.user

    try:
        event = Event.objects.get(event_id=event_id)

        res = event.add_interest(user.user_id)

        if res == 401:
            return Response(data={"message": "Try with a valid user."}, status=400)
        elif res == 402:
            return Response(data={"message": "Already sent request for the event."}, status=400)
        elif res == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(status=201)

    except Exception:
        return Response(data={"message": 'Try later.'}, status=500)
