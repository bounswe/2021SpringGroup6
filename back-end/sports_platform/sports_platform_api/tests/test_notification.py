from django.test import Client, TestCase
from .test_helper_functions import create_mock_user
from ..models.event_models import Event
from ..models.sport_models import Sport
from ..models.user_models import Follow
from ..helpers.geo import get_address
from rest_framework.authtoken.models import Token

class NotificationTest(TestCase):
    def setUp(self):
        self.client = Client()
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com','latitude':41,'longitude':39.7,
                     'sports':[{'sport':'soccer','skill_level':3}]}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}
        hamsi_info = {'identifier': 'hamsi',
                    'password': 'fish', 'email': 'hamsi@fish.com'}

        lion_user = create_mock_user(lion_info)
        cat_user = create_mock_user(cat_info)
        hamsi_user = create_mock_user(hamsi_info)
        self.token, _ = Token.objects.get_or_create(user=lion_user)
        Sport.objects.create(name="soccer")
        Follow.objects.create(follower=lion_user, following=cat_user)

        self.event_following = {
            "name": "lets play soccer",
            "sport": "soccer",
            "duration": 2,
            "startDate": "2021-12-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 5,
            "maximumAttendeeCapacity": 50,
            "maxSpectatorCapacity": 59,
            "minSkillLevel": 3,
            "acceptWithoutApproval": False,
            "maxSkillLevel": 5,
            "organizer": cat_user
        }

        self.event_location = {
            "name": "lets play soccer",
            "sport": "soccer",
            "duration": 2,
            "startDate": "2021-12-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 5,
            "maximumAttendeeCapacity": 50,
            "maxSpectatorCapacity": 59,
            "minSkillLevel": 3,
            "acceptWithoutApproval": False,
            "maxSkillLevel": 5,
            "organizer": hamsi_user
        }

        self.event_sport = {
            "name": "lets play soccer guys",
            "sport": "soccer",
            "duration": 2,
            "startDate": "2022-03-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 5,
            "maximumAttendeeCapacity": 50,
            "maxSpectatorCapacity": 59,
            "minSkillLevel": 3,
            "acceptWithoutApproval": False,
            "maxSkillLevel": 5,
            "organizer": hamsi_user
        }
        
        address_following = get_address(self.event_following["latitude"], self.event_following["longitude"])
        address_location = get_address(self.event_location["latitude"], self.event_location["longitude"])
        address_sport = get_address(self.event_sport["latitude"], self.event_sport["longitude"])

        self.response_following = {
            "event_id": 1,
            "name": self.event_following['name'],
            "sport": 'soccer',
            "duration":self.event_following['duration'],
            "startDate": "2021-12-13T13:00:00Z",
            "latitude": str(self.event_following['latitude']),
            "longitude": str(self.event_following['longitude']),
            "maximumAttendeeCapacity": self.event_following['maximumAttendeeCapacity'],
            "minimumAttendeeCapacity": self.event_following['minimumAttendeeCapacity'],
            "maxSpectatorCapacity": self.event_following['maxSpectatorCapacity'],
            "minSkillLevel": self.event_following['minSkillLevel'],
            "maxSkillLevel":self.event_following['maxSkillLevel'],
            "canEveryoneSeePosts": True,
            "canEveryonePostPosts": True,
            "description": "",
            "city": address_following['state'],
            "district": address_following['county'],
            "country": address_following['country'],
            "organizer": cat_user.user_id
        }

        self.response_location = {
            "event_id": 1,
            "name": self.event_location['name'],
            "sport": 'soccer',
            "duration":self.event_location['duration'],
            "startDate": "2021-12-13T13:00:00Z",
            "latitude": str(self.event_location['latitude']),
            "longitude": str(self.event_location['longitude']),
            "maximumAttendeeCapacity": self.event_location['maximumAttendeeCapacity'],
            "minimumAttendeeCapacity": self.event_location['minimumAttendeeCapacity'],
            "maxSpectatorCapacity": self.event_location['maxSpectatorCapacity'],
            "minSkillLevel": self.event_location['minSkillLevel'],
            "maxSkillLevel":self.event_location['maxSkillLevel'],
            "canEveryoneSeePosts": True,
            "canEveryonePostPosts": True,
            "description": "",
            "city": address_location['state'],
            "district": address_location['county'],
            "country": address_location['country'],
            "organizer": hamsi_user.user_id
        }

        self.response_sport = {
            "event_id": 1,
            "name": self.event_sport['name'],
            "sport": 'soccer',
            "duration":self.event_sport['duration'],
            "startDate": "2022-03-13T13:00:00Z",
            "latitude": str(self.event_sport['latitude']),
            "longitude": str(self.event_sport['longitude']),
            "maximumAttendeeCapacity": self.event_sport['maximumAttendeeCapacity'],
            "minimumAttendeeCapacity": self.event_sport['minimumAttendeeCapacity'],
            "maxSpectatorCapacity": self.event_sport['maxSpectatorCapacity'],
            "minSkillLevel": self.event_sport['minSkillLevel'],
            "maxSkillLevel":self.event_sport['maxSkillLevel'],
            "canEveryoneSeePosts": True,
            "canEveryonePostPosts": True,
            "description": "",
            "city": address_sport['state'],
            "district": address_sport['county'],
            "country": address_sport['country'],
            "organizer": hamsi_user.user_id
        }

        self.path = f"/recommendations"

    def test_success_following(self):
        event = Event.create_event(self.event_following)
        self.response_following['event_id'] = event['@id']
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.token}'})
        self.assertEqual(response.status_code, 200)
        response.data[0].pop('created_on')
        self.assertEqual(response.data[0], self.response_following)

    def test_success_location(self):
        event = Event.create_event(self.event_location)
        self.response_location['event_id'] = event['@id']
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.token}'})
        self.assertEqual(response.status_code, 200)
        response.data[0].pop('created_on')
        self.assertEqual(response.data[0], self.response_location)
    
    def test_success_sport(self):
        event = Event.create_event(self.event_sport)
        self.response_sport['event_id'] = event['@id']
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.token}'})
        self.assertEqual(response.status_code, 200)
        response.data[0].pop('created_on')
        self.assertEqual(response.data[0], self.response_sport)