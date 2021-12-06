from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Event
from ..validation import event_validation
from ..serializers.event_seralizer import EventSerializer


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


@api_view(['GET'])
def get_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        serialized = EventSerializer(event).data
        event_information = event.get_info()
        serialized.update(event_information)
    except Event.DoesNotExist:
        return Response(data={"message": 'Event id does not exist'}, status=400)
    except Exception as e:
        print(str(e))
        return Response(data={'message': 'An error occured, please try again later.'}, status=500)
    
    return Response(serialized, status=200)