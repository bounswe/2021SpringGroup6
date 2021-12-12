from django.test import Client, TestCase
from ..models import Event, EventParticipationRequesters, EventSpectators, EventParticipants, Sport
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from datetime import datetime, timezone

class UserParticipationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None


        dog_info = {'identifier': 'dog',
                    'password': 'barkbark', 'email': 'dog@bark.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.dog_user = create_mock_user(dog_info)
        self.cat_user = create_mock_user(cat_info)

        self.dog_token, _ = Token.objects.get_or_create(user=self.dog_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)

        authenticate(identifier=self.dog_user.identifier,
                     password=self.dog_user.password)

        event_data_1 = {
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": "2021-12-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.dog_user,
            "duration": 20
        }

        event_data_2 = {
            "name": "Basketball Time",
            "sport": "basketball",
            "startDate": "2021-09-18T15:00:00",
            "latitude": 56.002697,
            "longitude": 34.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 1,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 2,
            "acceptWithoutApproval": True,
            "organizer": self.dog_user,
            "duration": 34
        }

        event_data_3 = {
            "name": "Soccer Time 2",
            "sport": "soccer",
            "startDate": "2021-12-13T13:00:00",
            "latitude": 55.002697,
            "longitude": 55.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 1,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.dog_user,
            "duration": 45
        }

        Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")

        self.event_with_approval = Event.objects.get(event_id = Event.create_event(event_data_1)['@id'])

        self.event_without_approval = Event.objects.get(event_id=Event.create_event(event_data_2)['@id'])
        self.event_3 = Event.objects.get(event_id=Event.create_event(event_data_3)['@id'])

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        EventParticipants.objects.create(event = self.event_with_approval, user = self.dog_user, accepted_on = dt)
        EventParticipants.objects.create(event=self.event_without_approval, user=self.dog_user, accepted_on=dt)
        EventSpectators.objects.create(event = self.event_3, user=self.cat_user, requested_on = dt)
        EventSpectators.objects.create(event=self.event_without_approval, user=self.cat_user, requested_on=dt)
        EventParticipationRequesters.objects.create(event = self.event_with_approval, user = self.dog_user, requested_on = dt, message = "Please accept, I really like this sport.")
        EventParticipationRequesters.objects.create(event = self.event_3, user = self.dog_user, requested_on = dt, message = "Please accept, I really like this sport.")

        

        self.request_param = {'get_interested': self.dog_user.user_id,
                              'get_participating': self.dog_user.user_id,
                              'get_spectating': self.cat_user.user_id,
                              }

        self.request_token = {'get_interested': self.dog_token,
                              'get_participating': self.dog_token,
                              'get_spectating': self.dog_token
                              }

        self.response_bodies = {'get_interested': {
                                                        "@context": "https://schema.org/Person",
                                                        "@id": self.dog_user.user_id,
                                                        "identifier": self.dog_user.identifier,
                                                        "additionalProperty": {
                                                            "@type": "PropertyValue",
                                                            "name": "interestedEvents",
                                                            "value": [
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_with_approval.event_id,
                                                                    "name": self.event_with_approval.name,
                                                                    "sport": self.event_with_approval.sport.name,
                                                                    "startDate": self.event_with_approval.startDate,
                                                                    "location": self.event_with_approval._scheme_location()
                                                                },
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_3.event_id,
                                                                    "name": self.event_3.name,
                                                                    "sport": self.event_3.sport.name,
                                                                    "startDate": self.event_3.startDate,
                                                                    "location": self.event_3._scheme_location()
                                                                }
                                                            ]
                                                        }
                                                    },
                                'get_participating': {
                                                        "@context": "https://schema.org/Person",
                                                        "@id": self.dog_user.user_id,
                                                        "identifier": self.dog_user.identifier,
                                                        "additionalProperty": {
                                                            "@type": "PropertyValue",
                                                            "name": "participatingEvents",
                                                            "value": [
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_with_approval.event_id,
                                                                    "name": self.event_with_approval.name,
                                                                    "sport": self.event_with_approval.sport.name,
                                                                    "startDate": self.event_with_approval.startDate,
                                                                    "location": self.event_with_approval._scheme_location()
                                                                },
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_without_approval.event_id,
                                                                    "name": self.event_without_approval.name,
                                                                    "sport": self.event_without_approval.sport.name,
                                                                    "startDate": self.event_without_approval.startDate,
                                                                    "location": self.event_without_approval._scheme_location()
                                                                },
                                                            ]
                                                        }
                                                    },
                                'get_spectating': {
                                                        "@context": "https://schema.org/Person",
                                                        "@id": self.cat_user.user_id,
                                                        "identifier": self.cat_user.identifier,
                                                        "additionalProperty": {
                                                            "@type": "PropertyValue",
                                                            "name": "spectatingEvents",
                                                            "value": [
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_without_approval.event_id,
                                                                    "name": self.event_without_approval.name,
                                                                    "sport": self.event_without_approval.sport.name,
                                                                    "startDate": self.event_without_approval.startDate,
                                                                    "location": self.event_without_approval._scheme_location()
                                                                },
                                                                {
                                                                    "type": "https://schema.org/SportsEvent",
                                                                    "@id":  self.event_3.event_id,
                                                                    "name": self.event_3.name,
                                                                    "sport": self.event_3.sport.name,
                                                                    "startDate": self.event_3.startDate,
                                                                    "location": self.event_3._scheme_location()
                                                                }
                                                            ]
                                                        }
                                                    },
                                
                                }

        
    def test_get_interested(self):
        test_type = 'get_interested'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/interested"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})


        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 200)
        
    
    def test_get_participating(self):
        test_type = 'get_participating'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/participating"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_get_spectating(self):
        test_type = 'get_spectating'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/spectating"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

        

    