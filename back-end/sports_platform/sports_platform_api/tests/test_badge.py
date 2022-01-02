from django.test import Client, TestCase
from ..models import Event, Badge, UserBadges, EventBadges, EventParticipants, Sport
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
import datetime
from datetime import timezone, timedelta


class BadgeTest(TestCase):

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

        utc_dt = datetime.datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        event_data_1 = {
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": str(dt- timedelta(days=1)),
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
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": str(dt + timedelta(days=1)),
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

        s = Sport.objects.create(name="soccer")
        self.greed_badge = Badge.objects.create(name= "greed",wikidata= "Q12819497")
        self.competitive_badge = Badge.objects.create(name="competitive", wikidata="Q107289411")
        self.sport_badge = Badge.objects.create(name="football supporter", sport=s)

        self.event_with_approval = Event.objects.get(
            event_id=Event.create_event(event_data_1)['@id'])
        self.event_with_approval2 = Event.objects.get(
            event_id=Event.create_event(event_data_2)['@id'])

        
        EventParticipants.objects.create(
            event=self.event_with_approval, user=self.cat_user, accepted_on=dt)
        EventParticipants.objects.create(
            event=self.event_with_approval2, user=self.cat_user, accepted_on=dt)
        
        UserBadges.objects.create(
            user=self.cat_user, from_user=self.dog_user, badge=self.greed_badge, date=dt)
        EventBadges.objects.create(
            event=self.event_with_approval, badge=self.greed_badge, date=dt)
        

        self.request_param = {'give_other_user': self.dog_user.user_id,
                              'get_user': self.cat_user.user_id,
                              'get_event': self.event_with_approval.event_id,
                              'give_event': self.event_with_approval.event_id,
                              'already_given_event': self.event_with_approval.event_id,
                              'already_given_user': self.cat_user.user_id,
                              'badge_sport': "soccer",
                              'delete': self.event_with_approval.event_id
                              }

        self.request_token = {'give_other_user': self.cat_token,
                              'get_user': self.dog_token,
                              'get_event': self.dog_token,
                              'give_event': self.dog_token,
                              'already_given_user': self.dog_token,
                              'already_given_event': self.dog_token,
                              'badge_sport': self.dog_token,
                              'delete': self.dog_token,
                              }

        self.request_body = {
                            'give_other_user':{"badge":"competitive"},
                            'give_event': {"badge": "competitive"},
                            'already_given_user': {"badge": "greed"},
                            'already_given_event': {"badge": "greed"},
                            'delete': {"badge": "greed"},
                            }

        self.response_bodies = {'get_event': {
                                                "@context": "https://schema.org/SportsEvent",
                                                "@id": self.event_with_approval.event_id,
                                                "additionalProperty": {
                                                    "@type": "PropertyValue",
                                                    "name": "event_badges",
                                                    "value": [
                                                        {
                                                            "@context": "https://www.wikidata.org/entity/Q12819497",
                                                            "name": "greed"
                                                        }
                                                    ]
                                                }
                                            },
                                'get_user': {
                                                    "@context": "https://schema.org/Person",
                                                    "@id": self.cat_user.user_id,
                                                    "additionalProperty": [
                                                        {
                                                            "@type": "PropertyValue",
                                                            "name": "event_badges",
                                                            "value": [
                                                                {
                                                                    "@context": "https://www.wikidata.org/entity/Q12819497",
                                                                    "name": "greed",
                                                                    "additionalProperty": {
                                                                        "@type": "PropertyValue",
                                                                        "name": "event",
                                                                        "value": {
                                                                            "@context": "https://schema.org/SportsEvent",
                                                                            "@id": self.event_with_approval.event_id
                                                                        }
                                                                    }
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "@type": "PropertyValue",
                                                            "name": "user_badges",
                                                            "value": [{
                                                                "@context": "https://www.wikidata.org/entity/Q12819497",
                                                                "name": "greed",
                                                                "additionalProperty": {
                                                                    "@type": "PropertyValue",
                                                                    "name": "givenBy",
                                                                    "value": {
                                                                        "@context": "https://schema.org/Person",
                                                                        "@id": self.dog_user.user_id
                                                                    }
                                                                }
                                                            }]
                                                        }
                                                    ]
                                                },
                                'already_given_event': {"message": "Already added this badge to event."},
                                'already_given_user': {"message": "Already gave this badge to this user."},
                                'badge_sport':{
                                    'badges' : [{
                                        "name": "football supporter",
                                        "sport": "soccer"
                                    }]
                                }

        }

    def test_give_other_user(self):
        test_type = 'give_other_user'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/badges"

        request_body = self.request_body[test_type]

        response = self.client.post(
            path, request_body,  content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(UserBadges.objects.filter(
            from_user=self.dog_user, user=self.cat_user, badge="greed").exists())

    def test_give_event(self):
        test_type = 'give_event'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/badges"

        request_body = self.request_body[test_type]

        response = self.client.post(
            path, request_body,  content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EventBadges.objects.filter(
            event=self.event_with_approval, badge="greed").exists())
    
    def test_get_event(self):
        test_type = 'get_event'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/badges"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_badge_sport(self):
        test_type = 'badge_sport'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/badges/" + str(request_param) 

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_get_user(self):
        test_type = 'get_user'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/badges"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])


    def test_already_given_event(self):
        test_type = 'already_given_event'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/badges"

        request_body = self.request_body[test_type]

        response = self.client.post(
            path, request_body,  content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)
        
    def test_already_given_user(self):
        test_type = 'already_given_user'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/badges"

        request_body = self.request_body[test_type]

        response = self.client.post(
            path, request_body,  content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)
        
    def test_delete(self):
        test_type = 'delete'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/badges"

        request_body = self.request_body[test_type]

        response = self.client.delete(
            path, request_body,  content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EventBadges.objects.filter(
            event=self.event_with_approval, badge=self.greed_badge).exists())
