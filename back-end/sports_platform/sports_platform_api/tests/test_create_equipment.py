from django.test import Client, TestCase
from ..models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from ..models import Equipment, Sport


class CreateEquipmentTest(TestCase):

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
            "name": "soccer ball",
            "sport": "soccer",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "description": "soccer ball at Trabzon"
        }

        self.response = {
            "@context": "https://schema.org/Product",
            "@id": 1,
            "name": "soccer ball",
            "sport": {
                "@type": "Thing",
                "name": "soccer"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 41.002697,
                "longitude": 39.716763
            },
            "description": "soccer ball at Trabzon",
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "created_on",
                    "value": "2021-12-30T19:00:49.487619Z"
                }
            ],
            "creator": {
                "@type": "Person",
                "@id": self.cat_user.user_id,
                "identifier":self.cat_user.identifier 
            }
        }

        self.response_bodies = {'no_name': {"message": {"name": ["This field is required."]}},
                                'wrong_sport': {"message": "Enter a valid sport."},
                                'wrong_coordinate': {"message": {"latitude": ["Ensure this value is less than or equal to 90."], "longitude": ["Ensure this value is greater than or equal to -180."]}},
                                }

        self.path = '/equipments'
        self.maxDiff = None

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

    def test_success(self):
        request_body = self.request_body
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})

        self.assertEqual(response.data['@context'], "https://schema.org/Product")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Equipment.objects.filter(
            equipment_id=response.data['@id']).exists())
        self.assertEqual(Equipment.objects.get(
            equipment_id=response.data['@id']).name, request_body['name'])


        response = self.client.get(
            self.path+"/"+str(response.data['@id']), content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})

        self.assertEqual(response.status_code, 200)
        res_body = self.response
        res_body['@id'] = response.data['@id']
        res_body['additionalProperty'][0]['value'] = Equipment.objects.get(equipment_id=response.data['@id']).created_on
        self.assertEqual(response.data, res_body)


        