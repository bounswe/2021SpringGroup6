from django.test import Client, TestCase
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user
from ..models import Sport, Event, EventParticipants,EventSpectators, SportSkillLevel
import datetime

class UpdateEventTest(TestCase):
    def setUp(self):
        self.client = Client()
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}
        self.cat_user = create_mock_user(cat_info)

        self.user = create_mock_user({'identifier':'lion', 'password': 'roarroar', 'email': 'lion@roar.com'})
        self.user_token, _ = Token.objects.get_or_create(user=self.user)
        
        soccer = Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")
        SportSkillLevel.objects.create(user=self.user, sport=soccer, skill_level=3)
        event_info1 = {
            "name": "lets play soccer",
            "sport":'soccer',
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
            "organizer": self.user
        }
        event = Event.create_event(event_info1)
        self.event = Event.objects.filter(pk=event['@id'])[0]
        self.header = {'HTTP_AUTHORIZATION': f'Token {self.user_token}'}
        self.path = f'/events/{self.event.event_id}'
        self.update_info = {'description':'come onn!'}
        self.update_info_part = {'maximumAttendeeCapacity':1}
        self.update_info_spec = {'maxSpectatorCapacity':1}
        self.update_skill = {'minSkillLevel':4}

    def test_success(self):
        response = self.client.put(self.path,content_type='application/json', data=self.update_info, **self.header)
        self.assertEqual(response.status_code, 200)
    
    def test_more_participant(self):
        utc_dt = datetime.datetime.now(datetime.timezone.utc)  
        dt = utc_dt.astimezone()
        EventParticipants.objects.create(user=self.user,event=self.event,accepted_on=dt)
        EventParticipants.objects.create(user=self.cat_user,event=self.event,accepted_on=dt)
        response = self.client.put(self.path,content_type='application/json', data=self.update_info_part, **self.header)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"message": 'There are more participants than requested maximumAttendeeCapacity.'})
    
    def test_more_spectators(self):
        utc_dt = datetime.datetime.now(datetime.timezone.utc)  
        dt = utc_dt.astimezone()
        EventSpectators.objects.create(user=self.user,event=self.event,requested_on=dt)
        EventSpectators.objects.create(user=self.cat_user,event=self.event,requested_on=dt)
        response = self.client.put(self.path,content_type='application/json', data=self.update_info_spec, **self.header)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"message": 'There are more spectators than requested maxSpectatorCapacity.'})

    def test_skill_level(self):
        utc_dt = datetime.datetime.now(datetime.timezone.utc)  
        dt = utc_dt.astimezone()
        EventParticipants.objects.create(user=self.user,event=self.event,accepted_on=dt)
        response = self.client.put(self.path,content_type='application/json', data=self.update_skill, **self.header)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"message": 'There is a participant with lower skill level than requested minSkillLevel.'})