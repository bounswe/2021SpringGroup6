from django.test import Client, TestCase
from .test_helper_functions import create_mock_user
from ..models.event_models import Event
from ..models.sport_models import Sport
from ..helpers.geo import get_address

class GetEventTest(TestCase):
    def setUp(self):
        self.client = Client()
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}

        lion_user = create_mock_user(lion_info)
        Sport.objects.create(name="soccer")

        event_info = {
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
            "organizer": lion_user
        }
        event = Event.create_event(event_info)
        address = get_address(event_info["latitude"], event_info["longitude"])
        
        self.response_body = {
            "event_id": event['@id'],
            "@context": "https://schema.org",
            "@type": "SportsEvent",
            "name": "lets play soccer",
            "sport": "soccer",
            "startDate": "2021-12-13T13:00:00",
            "location":{
                "@context": "https://schema.org",
                "@type": "Place",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": event_info["latitude"],
                    "longitude": event_info["longitude"]
                },
                "address": f'{address["county"]}, {address["state"]}, {address["country"]}'
            },
            "maximumAttendeeCapacity": 50,
            "attendee": [],
            "organizer": {
                "@context": "https://schema.org",
                "@type": "Person",
                "@id":lion_user.user_id 
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
                "name": "spectator",
                "value":[]
                }
            ]
        }

        self.path = f"/events/{event['@id']}"

        self.invalid_path = f'/events/100'

    def test_success(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_body)

    def test_not_exist_event(self):
        response = self.client.get(self.invalid_path)
        self.assertEqual(response.status_code, 400)