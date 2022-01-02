import copy
from django.test import Client, TestCase
from ..models import Equipment, Sport
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user
from ..helpers.geo import get_address


class SearchEquipmentTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)

        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)

        Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")

        equipment_info1 = {
            "name": "soccer ball",
            "sport": "soccer",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "description": "soccer ball at Trabzon"
        }

        equipment_info2 = {
            "name": "basket ball",
            "sport": "basketball",
            "latitude": 50.002697,
            "longitude": 50.716763,
            "description": "cheap basketball"
        }

        self.equipment1 = Equipment.create_equipment(equipment_info1, self.lion_user)
        self.equipment1 = Equipment.objects.get(equipment_id = self.equipment1['@id'])
        self.equipment2 = Equipment.create_equipment(equipment_info2, self.cat_user)
        self.equipment2 = Equipment.objects.get(equipment_id = self.equipment2['@id'])


        base_response = {'@context': "https://www.w3.org/ns/activitystreams", 'type': 'OrderedCollection',
                         'total_items': 1}
        
        self.request_bodies = {'missing_latitude': {'latitudeBetweenStart': 40.456},
                               'missing_longitude': {'longitudeBetweenEnd': 40.456},
                               'filter_sport': {'sport': 'soccer'},
                               'filter_name': {'nameContains': 'soc'},
                               'filter_creator': {'creator': self.cat_user.user_id},
                               'filter_latitude': {'latitudeBetweenStart': 40, 'latitudeBetweenEnd': 50},
                               'filter_latitude2': {'latitudeBetweenStart': 40, 'latitudeBetweenEnd': 52}
                               }

        equipment1_response = base_response.copy()
        equipment1_response['items'] = [self.equipment1.get_equipment()]

        equipment2_response = base_response.copy()
        equipment2_response['items'] = [self.equipment2.get_equipment()]

        combined_response = base_response.copy()
        combined_response['total_items'] = 2
        combined_response['items'] = [
            self.equipment2.get_equipment(), self.equipment1.get_equipment()]

        self.response_bodies = {'missing_latitude': {"message": {"latitude": ["latitudeBetweenStart and latitudeBetweenEnd must be given together."]}},
                                'missing_longitude': {"message": {"longitude": ["longitudeBetweenStart and longitudeBetweenEnd must be given together."]}},
                                'filter_sport': equipment1_response,
                                'filter_name': equipment1_response,
                                'filter_latitude': equipment1_response,
                                'filter_latitude2': combined_response,
                                'filter_creator': equipment2_response}

        self.path = '/equipments/searches'

    def test_filter_sport(self):
        test_type = 'filter_sport'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_filter_name(self):
        test_type = 'filter_name'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])


    def test_filter_latitude(self):
        test_type = 'filter_latitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_filter_latitude2(self):
        test_type = 'filter_latitude2'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_filter_creator(self):
        test_type = 'filter_creator'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})


        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_missing_latittude(self):
        test_type = 'missing_latitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_missing_longitude(self):
        test_type = 'missing_longitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{
                                    'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    

 