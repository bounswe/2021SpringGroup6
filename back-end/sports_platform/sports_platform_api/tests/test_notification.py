from django.test import Client, TestCase
from rest_framework.authtoken.models import Token
from ..models import Notification,Sport, Event
from .test_helper_functions import create_mock_user
from datetime import datetime, timezone, timedelta

class NotificationTest(TestCase):
    def setUp(self):
        self.client = Client()
        lion = {'identifier':'lion', 'password': 'roarroar', 'email': 'lion@roar.com'}
        lion_user = create_mock_user(lion)

        Sport.objects.create(name="soccer")
        self.lion_token, _ = Token.objects.get_or_create(user=lion_user)

        event_info = {
            "name": "lets play soccer",
            "sport": "soccer",
            "duration": 2,
            "startDate": "2021-12-31T13:00:00",
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
        event = Event.objects.get(event_id = Event.create_event(event_info)['@id'])
        utc_dt = datetime.now().date()
        previous_dt = utc_dt - timedelta(days=5)
        notification_spot = Notification.objects.create(event_id=event, user_id=lion_user, date=previous_dt,notification_type=f'3 Spots Left')
        notification_event_full = Notification.objects.create(event_id=event, user_id=lion_user, date=utc_dt,notification_type=f'Event Full')


        self.path = f'/notifications'
        self.response = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Notifications",
            "type": "Collection",
            "total_items": 2,
            "Items":[{
            "description": f"only 3 spots left for the event with name lets play soccer",
            "notification_id": notification_spot.id,
            "event_id": event.event_id,
            "date": notification_spot.date,
            "type": "Few Spots Left for an Event"
            },
            {
            "description": f"The event with name lets play soccer is full now.",
            "notification_id": notification_event_full.id,
            "event_id": event.event_id,
            "date": notification_event_full.date,
            "type": notification_event_full.notification_type
            }]
            }
        self.read_path = f'/notifications/{notification_spot.id}'
        self.read_response = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Notifications",
            "type": "Collection",
            "total_items": 1,
            "Items":[
            {
            "description": f"The event with name lets play soccer is full now.",
            "notification_id": notification_event_full.id,
            "event_id": event.event_id,
            "date": notification_event_full.date,
            "type": notification_event_full.notification_type
            }]
            }

    def test_get_success(self):
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response)
    
    def test_read_success(self):
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response)

        read_response = self.client.post(self.read_path, **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        self.assertEqual(read_response.status_code, 200)
        response = self.client.get(self.path, **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.read_response)




