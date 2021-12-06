from django.test import Client, TestCase
from ..models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from ..models import Event, Sport

class CreateEventTest(TestCase):

    def setUp(self):
        self.client = Client()

        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.cat_user = create_mock_user(cat_info)

        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)

        authenticate(identifier=self.cat_user.identifier,
                     password=self.cat_user.password)

        Sport.objects.create(name="soccer")

        self.request_body = {
                                    "name": "lets play soccer",
                                    "sport": "soccer",
                                    "startDate": "2021-12-13T13:00:00",
                                    "latitude": 41.002697,
                                    "longitude": 39.716763,
                                    "minimumAttendeeCapacity": 5,
                                    "maximumAttendeeCapacity": 50,
                                    "maxSpectatorCapacity": 59,
                                    "minSkillLevel": 3,
                                    "maxSkillLevel": 5,
                                    "acceptWithoutApproval": False
                                }


        self.response_bodies = {'no_name': {"message": {"name": ["This field is required."]}},
                                'wrong_sport': {"message": "Enter a valid sport."},
                                'wrong_coordinate': {"message": {"latitude": ["Ensure this value is less than or equal to 90."],"longitude": ["Ensure this value is greater than or equal to -180."]}},
                                
                                'bigger_min_skill': {"message": {"skillLevel": ["minSkillLevel should be smaller than or equal to maxSkillLevel"]}},
                                'wrong_date': {"message": {"startDate": [
                                    "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
                                ]}}
                                }

        self.path = '/events'
        self.maxDiff=None


    def test_no_name(self):
        test_type = 'no_name'
        request_body = self.request_body
        del request_body['name']
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_wrong_sport(self):
        test_type = 'wrong_sport'
        request_body = self.request_body
        request_body['sport'] = "non-existing_sport"
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_wrong_coordinate(self):
        test_type = 'wrong_coordinate'
        request_body = self.request_body
        request_body['latitude'] = 91
        request_body['longitude'] = -191
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_bigger_min_skill(self):
        test_type = 'bigger_min_skill'
        request_body = self.request_body
        request_body['minSkillLevel'] = 5
        request_body['maxSkillLevel'] = 3
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_wrong_date(self):
        test_type = 'wrong_date'
        request_body = self.request_body
        request_body['startDate'] = "June 13"
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_success(self):
        request_body = self.request_body
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})

        self.assertEqual(response.data['@context'], "https://schema.org/SportsEvent")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Event.objects.get(event_id = response.data['@id']).name, request_body['name'])