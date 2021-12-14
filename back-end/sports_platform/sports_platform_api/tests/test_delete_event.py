from django.test import Client, TestCase
from .test_helper_functions import create_mock_user
from ..models.event_models import Event
from ..models.sport_models import Sport
from rest_framework.authtoken.models import Token

class DeleteEventTest(TestCase):
    def setUp(self):
        self.client = Client()
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        lion_user = create_mock_user(lion_info)
        cat_user = create_mock_user(cat_info)

        self.lion_token, _ = Token.objects.get_or_create(user=lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=cat_user)
        Sport.objects.create(name="soccer")

        event_info = {
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
            "organizer": lion_user
        }
        event = Event.create_event(event_info)

        self.path = f"/events/{event['@id']}"

        self.invalid_path = f'/events/100'

    def test_success(self):
        response = self.client.delete(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        self.assertEqual(response.status_code, 204)

    def test_not_exist_event(self):
        response = self.client.get(self.invalid_path)
        self.assertEqual(response.status_code, 400)
    
    def test_not_authorized(self):
        response = self.client.delete(self.path)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'User not logged in.')
    
    def test_delete_another(self):
        response = self.client.delete(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.cat_token}'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Only organizers can delete events.")
    