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


@api_view(['POST', 'GET', 'DELETE'])
def attend_spectator(request, event_id):

    if request.method == 'POST':
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
            elif res == 404:
                return Response(data={"message": "Registered as participant to this event, if being spectator is wanted, remove participating status."}, status=400)
            elif res == 404:
                return Response(data={"message": "Showed interest to participate this event. If spectator status is wanted remove the interest."}, status=400)
            elif res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=201)

        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception:
            return Response(data={"message": 'Try later.'}, status=500)

    elif request.method == 'GET':
        try:
            event = Event.objects.get(event_id=event_id)

            res = event.get_participants()
            event_dict = dict()
            event_dict['@context'] = "https://schema.org/SportsEvent"
            event_dict['@id'] = event.event_id

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                event_dict['audience'] = res
                return Response(data=event_dict, status=200)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)

    elif request.method == 'DELETE':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.delete_spectator(user)

            if res == 401:
                return Response(data={"message": "Not a spectator for this event"}, status=400)
            if res == 500:
                return Response(data={"message": 'Try later.'}, status=500)
            else:
                return Response(status=204)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['POST', 'GET', 'DELETE'])
def add_interest(request, event_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = event_validation.Request_Message(data=request.data)

        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)

        validated_body = validation.validated_data

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.add_interest(user.user_id, validated_body)

            if res == 401:
                return Response(data={"message": "Try with a valid user."}, status=400)
            elif res == 402:
                return Response(data={"message": "Already sent request for the event."}, status=400)
            elif res == 403:
                return Response(data={"message": "Participant capacity is full for this event."}, status=400)
            elif res == 404:
                return Response(data={"message": "Already participating the event."}, status=400)
            elif res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=201)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            print("hey")
            print(e)
            return Response(data={"message": 'Try later.'}, status=500)

    elif request.method == 'GET':

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.get_interesteds()

            event_dict = dict()
            event_dict['@context'] = "https://schema.org/SportsEvent"
            event_dict['@id'] = event.event_id


            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                event_dict['additionalProperty'] = {
                    "@type": "PropertyValue",
                    "name": "interesteds",
                    "value": res
                }
                return Response(data=event_dict, status=200)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            print("hey")
            print(e)
            return Response(data={"message": 'Try later.'}, status=500)

    elif request.method == 'DELETE':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.delete_interest(user)

            if res == 401:
                return Response(data={"message": "Not interested for this event"}, status=400)
            if res == 500:
                return Response(data={"message": 'Try later.'}, status=500)
            else:
                return Response(status=204)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)
def accept_participant(request, event_id):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    user = request.user

    validation = event_validation.Accept_Participant(data=request.data)
    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    try:
        event = Event.objects.get(event_id=event_id)

        if event.organizer.user_id != user.user_id:
            return Response(data={"message": "Only organizers can accept users for the event."}, status=403)

        res = event.add_participant(validation.validated_data['user_id_list'])

        if res == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(data = res, status=200)
    except Event.DoesNotExist:
        return Response(data={"message": "Try with a valid event."}, status=400)
    except Exception as e:
        print(e)
        return Response(data={"message": 'Try later.'}, status=500)
