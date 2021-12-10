import copy
from django.test import Client, TestCase
from ..models import Event, Sport
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user
from ..helpers.geo import get_address

class SearchEventTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        lion_user = create_mock_user(lion_info)
        cat_user = create_mock_user(cat_info)

        self.lion_token, _ = Token.objects.get_or_create(user=lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=cat_user)

        Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")

        event_info1 = {
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
            "maxSkillLevel": 4,
            "organizer": lion_user
        }

        event_info2 = {
            "name": "lets play basketball",
            "sport": "basketball",
            "duration": 2,
            "startDate": "2021-10-13T13:00:00",
            "latitude": 12.002697,
            "longitude": 32.716763,
            "minimumAttendeeCapacity": 5,
            "maximumAttendeeCapacity": 50,
            "maxSpectatorCapacity": 59,
            "minSkillLevel": 5,
            "acceptWithoutApproval": False,
            "maxSkillLevel": 5,
            "organizer": lion_user
        }
        event = Event.create_event(event_info1)
        address = get_address(event_info1["latitude"], event_info1["longitude"])

        base_response =  {'@context':"https://www.w3.org/ns/activitystreams", 'type':'Collection',
                          'total_items':1}
        event1 = {
            "event_id": event['@id'],
            "@context": "https://schema.org",
            "@type": "SportsEvent",
            "name": "lets play soccer",
            "sport": "soccer",
            "duration": 2,
            "startDate": "2021-12-13T13:00:00Z",
            "location":{
                "@context": "https://schema.org",
                "@type": "Place",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": event_info1["latitude"],
                    "longitude": event_info1["longitude"]
                },
                "address": f'{address["county"]}, {address["state"]}, {address["country"]}'
            },
            "maximumAttendeeCapacity": 50,
            "minSkillLevel":3,
            "maxSkillLevel": 4,
            "attendee": [],
            "audience" : [],
            "organizer": {
                "@context": "https://schema.org",
                "@type": "Person",
                "@id":lion_user.user_id ,
                "identifier":lion_user.identifier
            },
            "description": "",
            "additionalProperty": [
                {
                "@type": "PropertyValue",
                "name": "minimumAttendeeCapacity",
                "value": 5
                },
                {
                "@type": "PropertyValue",
                "name": "maxSpectatorCapacity",
                "value": 59
                },
                {
                "@type": "PropertyValue",
                "name": "interesteds",
                "value": []
                },
                {
                "@type": "PropertyValue",
                "name": "acceptWithoutApproval",
                "value": False
                }
            ]
        }
        event = Event.create_event(event_info2)
        address = get_address(event_info2["latitude"], event_info2["longitude"])
        event2 = {
            "event_id": event['@id'],
            "@context": "https://schema.org",
            "@type": "SportsEvent",
            "name": "lets play basketball",
            "sport": "basketball",
            "duration": 2,
            "startDate": "2021-10-13T13:00:00Z",
            "location":{
                "@context": "https://schema.org",
                "@type": "Place",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": event_info2["latitude"],
                    "longitude": event_info2["longitude"]
                },
                "address": f'{address["county"]}, {address["state"]}, {address["country"]}'
            },
            "maximumAttendeeCapacity": 50,
            "minSkillLevel":5,
            "maxSkillLevel": 5,
            "attendee": [],
            "audience" : [],
            "organizer": {
                "@context": "https://schema.org",
                "@type": "Person",
                "@id":lion_user.user_id ,
                "identifier":lion_user.identifier
            },
            "description": "",
            "additionalProperty": [
                {
                "@type": "PropertyValue",
                "name": "minimumAttendeeCapacity",
                "value": 5
                },
                {
                "@type": "PropertyValue",
                "name": "maxSpectatorCapacity",
                "value": 59
                },
                {
                "@type": "PropertyValue",
                "name": "interesteds",
                "value": []
                },
                {
                "@type": "PropertyValue",
                "name": "acceptWithoutApproval",
                "value": False
                }
            ]
        }
        event1_response = copy.deepcopy(base_response)
        all_response = copy.deepcopy(base_response)
        event1_response['items'] = [event1]
        all_response['items'] = [event2, event1]
        all_response['total_items'] = 2
        self.request_bodies = {'missing_latitude': {'latitudeBetweenStart': 40.456},
                               'missing_longitude': {'longitudeBetweenEnd': 40.456},
                               'time_conradiction': {'timeBetweenStart':'15:00:00.000', 'timeBetweenEnd':'14:00:00.000'},
                               'coordinate_city_together': {'longitudeBetweenEnd': 40.456,'longitudeBetweenStart': 32.456,'city':'Izmir'},
                               'filter_sport':{'sport':'soccer'},
                               'filter_name':{'nameContains':'soc'},
                               'filter_date': {'dateBetweenStart':'2021-12-13'},
                               'filter_skill':{'skillLevel':[3,4]},
                               'filter_organizer':{'creator':lion_user.user_id},
                               'filter_latitude':{'latitudeBetweenStart':40, 'latitudeBetweenEnd':50}
                               }

        self.response_bodies = {'missing_latitude': {"message": {"latitude": ["latitudeBetweenStart and latitudeBetweenEnd must be given together."]}},
                                'missing_longitude': {"message": {"longitude": ["longitudeBetweenStart and longitudeBetweenEnd must be given together."]}},
                                'time_conradiction': {"message": {"time": ["timeBetweenStart should be smaller than or equal to timeBetweenEnd"]}},
                                'coordinate_city_together': {"message": {"city": ["city and coordinate information must not be given together"]}},
                                'filter_sport':event1_response,
                                'filter_name':event1_response,
                                'filter_date': event1_response,
                                'filter_skill':event1_response,
                                'filter_latitude':event1_response,
                                'filter_organizer':all_response
                                }

        self.path = '/events/searches'

    def test_filter_sport(self):
        test_type = 'filter_sport'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_name(self):
        test_type = 'filter_name'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_date(self):
        test_type = 'filter_date'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_skill(self):
        test_type = 'filter_skill'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_latitude(self):
        test_type = 'filter_latitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_organizer(self):
        test_type = 'filter_organizer'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        for index,_ in enumerate(response.data['items']):
            response.data['items'][index].pop('created_on')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_missing_latittude(self):
        test_type = 'missing_latitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_missing_longitude(self):
        test_type = 'missing_longitude'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_time_conradiction(self):
        test_type = 'time_conradiction'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_coordinate_city_together(self):
        test_type = 'coordinate_city_together'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
