from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Event, DiscussionPost, DiscussionComment, EventBadges, Badge
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


@api_view(['GET', 'DELETE', 'PUT'])
def get_event(request, event_id):
    if request.method == 'GET':
        try:
            event = Event.objects.get(pk=event_id)
            seralized = EventSerializer(event).data
            event_information = event.get_info()
            seralized.update(event_information)
        except Event.DoesNotExist:
            return Response(data={"message": 'Event id does not exist'}, status=400)
        except Exception:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)
        
        return Response(seralized, status=200)
    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)
        try:
            event = Event.objects.get(event_id = event_id)   

            if event.organizer.user_id != request.user.user_id:
                return Response(data={"message": "Only organizers can delete events."}, status=403)
            
            with transaction.atomic():
                event.delete()
            return Response(status=204)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception:
            return Response(data={"message": 'Try later.'}, status=500)
    elif request.method == 'PUT':
        if not request.user.is_authenticated:
            return Response({"message": "Login required."},
                        status=401)

        validation = event_validation.Update(data=request.data)
        if not validation.is_valid():
            return Response(data = {"message": validation.errors}, status=400)
        try:
            event = Event.objects.get(event_id=event_id)
            if event.organizer.user_id != request.user.user_id:
                return Response(data={"message": 'Only organizers can update the event.'}, status=403)
            return_code = event.update(validation.validated_data)
            if return_code == 400:
                return Response(data={"message": 'There are more participants than requested maximumAttendeeCapacity.'}, status=400)
            if return_code == 401:
                return Response(data={"message": 'There is a participant with lower skill level than requested minSkillLevel.'}, status=400)
            if return_code == 402:
                return Response(data={"message": 'There is a participant with higher skill level than requested maxSkillLevel.'}, status=400)
            if return_code == 403:
                return Response(data={"message": 'There are more spectators than requested maxSpectatorCapacity.'}, status=400)
            if return_code == 200:
                return Response(status=200)
            else:
                return Response(data={'message': 'An error occured, please try again later.'}, status=500)

        except Event.DoesNotExist:
            return Response(data={"message": 'Event id does not exist'}, status=400)
        except Exception as e:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)

    
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

            if res == 201:
                return Response(data={"message": "Added as spectator but spectator capacity is full."}, status=201)
            elif res == 401:
                return Response(data={"message": "Try with a valid user."}, status=400)
            elif res == 402:
                return Response(data={"message": "Already a spectator for the event."}, status=400)
            elif res == 404:
                return Response(data={"message": "Registered as participant to this event, if being spectator is wanted, remove participating status."}, status=400)
            elif res == 404:
                return Response(data={"message": "Showed interest to participate this event. If spectator status is wanted remove the interest."}, status=400)
            elif res == 408:
                return Response(data={"message": "Event start time is passed."}, status=400)
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

            res = event.get_spectators()
            event_dict = dict()
            event_dict['@context'] = "https://schema.org/SportsEvent"
            event_dict['@id'] = event.event_id

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                event_dict['audience'] = res
                return Response(data=event_dict, status=200)

        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
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
            elif res == 405:
                return Response(data={"message": "Registered as spectator to this event, if being participant is wanted, remove spectating status."}, status=400)
            elif res == 406:
                return Response(data={"message": "No skill level is entered for the sport."}, status=400)
            elif res == 407:
                return Response(data={"message": "User skill level does not match the requirements for the event."}, status=400)
            elif res == 408:
                return Response(data={"message": "Event start time is passed."}, status=400)
            elif res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=201)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
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
            elif res == 400:
                return Response(data={"message": "This event does not require organizer approval to participate."}, status=400)
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


@api_view(['POST', 'GET', 'DELETE'])
def accept_participant(request, event_id):

    if request.method == 'POST':
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

            res = event.add_participant(
                validation.validated_data['accept_user_id_list'], validation.validated_data['reject_user_id_list'])

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            elif res == 408:
                return Response(data={"message": "Event start time is passed."}, status=400)
            if res == 401:
                return Response(data={"message": "This event accepts participants without approval."}, status=400)
            else:
                return Response(data = res, status=201)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
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
                event_dict['attendee'] = res
                return Response(data=event_dict, status=200)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)

    elif request.method == 'DELETE':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.delete_participant(user)

            if res == 401:
                return Response(data={"message": "Not participanting for this event"}, status=400)
            if res == 500:
                return Response(data={"message": 'Try later.'}, status=500)
            else:
                return Response(status=204)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['POST'])
def search_event(request):
    validation = event_validation.Search(data=request.data)

    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    validated_body = validation.validated_data
    events = Event.search_event(validated_body, request.user)
    response = {'@context':"https://www.w3.org/ns/activitystreams", 'type':'OrderedCollection',
                'total_items':len(events),'items':[]}
    
    for event in events:
        seralized = EventSerializer(event).data
        event_information = event.get_info()
        seralized.update(event_information)
        response['items'].append(seralized)

    return Response(response, status=200)


@api_view(['GET','POST','DELETE'])
def get_badges(request, event_id):

    if request.method == 'GET':
        try:
            event = Event.objects.get(event_id=event_id)

            badges = event.get_badges()

            if badges == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(data=badges, status=200)
        except Event.DoesNotExist:
            return Response(data={"message": "Event does not exist."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)

    elif request.method == 'POST':

        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        try:
            
            event = Event.objects.get(event_id=event_id)

            if event.organizer.user_id != current_user.user_id:
                return Response(data={"message": "Only organizers can add badges to event."}, status=403)


            validation = event_validation.Badge(data=request.data)
            if not validation.is_valid():
                return Response(validation.errors, status=400)

            badge = validation.validated_data['badge']

            badges = event.add_badge(badge)

            if badges == 401:
                return Response(data={"message": "Enter a valid badge."}, status=400)
            elif badges == 402:
                return Response(data={"message": "Already added this badge to event."}, status=400)
            elif badges == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=201)
        except Event.DoesNotExist:
            return Response(data={"message": "Event does not exist."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)

    elif request.method == 'DELETE':

        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        try:

            event = Event.objects.get(event_id=event_id)

            if event.organizer.user_id != current_user.user_id:
                return Response(data={"message": "Only organizers can delete badges to event."}, status=403)

            validation = event_validation.Badge(data=request.data)
            if not validation.is_valid():
                return Response(validation.errors, status=400)

            badge = Badge.objects.get(name=validation.validated_data['badge'])


            event_badge = EventBadges.objects.get(
                event=event, badge=badge)

            with transaction.atomic():
                event_badge.delete()
            return Response(status=204)

        except Event.DoesNotExist:
            return Response(data={"message": "Event does not exist."}, status=400)
        except Badge.DoesNotExist:
            return Response(data={"message": "Badge does not exist."}, status=400)
        except EventBadges.DoesNotExist:
            return Response(data={"message": "Badge does not exist for that event."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)


@api_view(['POST', 'GET'])
def post_post(request, event_id):

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = event_validation.DiscussionPost(data=request.data)
        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)

        try:
            res = DiscussionPost.create_post(validation.validated_data, user, event_id)

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            if res == 401:
                return Response(data={"message": "Only participants and spectators can post posts."}, status=400)
            if res == 402:
                return Response(data={"message": "Enter a valid event."}, status=400)
            else:
                return Response(data=res, status=201)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)
    
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            event = Event.objects.get(event_id=event_id)

            res = event.get_posts(user)

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            if res == 401:
                return Response(data={"message": "Only participants and spectators can see posts."}, status=400)
            else:
                return Response(data=res, status=200)
        except Event.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['DELETE','POST'])
def delete_post_post(request, event_id, post_id):

    if request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            post = DiscussionPost.objects.get(post_id = post_id)

            if post.event.event_id != event_id:
                return Response(data={"message": "This post does not belong to that event_id."}, status=400)

            if user.user_id != post.event.organizer.user_id and user.user_id != post.author.user_id :
                return Response(data={"message": "Only post authors and event creators can delete posts."}, status=400)

            try:
                with transaction.atomic():
                    post.delete()
                return Response(status=204)
            except:
                return Response(data={"message": "Try later."}, status=500)

        except DiscussionPost.DoesNotExist:
            return Response(data={"message": "Try with a valid discussion post."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = event_validation.DiscussionComment(data=request.data)
        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)

        try:
            post = DiscussionPost.objects.get(post_id=post_id)

            if post.event.event_id != event_id:
                return Response(data={"message": "This post does not belong to that event_id."}, status=400)

            res = post.comment_post(validation.validated_data, user)

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            if res == 401:
                return Response(data={"message": "Only participants and spectators can post posts."}, status=400)
            else:
                return Response(status=201)
        except DiscussionPost.DoesNotExist:
            return Response(data={"message": "Try with a valid event."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)
    

@api_view(['DELETE'])
def delete_comment(request, event_id, post_id, comment_id):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    user = request.user

    try:
        comment = DiscussionComment.objects.get(comment_id=comment_id)

        if comment.post.event.event_id != event_id:
            return Response(data={"message": "This comment does not belong to that event_id."}, status=400)

        if comment.post.post_id != post_id:
            return Response(data={"message": "This comment does not belong to that post_id."}, status=400)

        if user.user_id != comment.post.event.organizer.user_id and user.user_id != comment.author.user_id:
            return Response(data={"message": "Only comment authors and event creators can delete posts."}, status=400)

        try:
            with transaction.atomic():
                comment.delete()
            return Response(status=204)
        except:
            return Response(data={"message": "Try later."}, status=500)

    except DiscussionComment.DoesNotExist:
        return Response(data={"message": "Try with a valid discussion comment."}, status=400)
    except Exception as e:
        return Response(data={"message": 'Try later.'}, status=500)
