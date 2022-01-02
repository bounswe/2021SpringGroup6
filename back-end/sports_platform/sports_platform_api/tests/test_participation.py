from django.test import Client, TestCase
from ..models import Event, EventParticipationRequesters, EventSpectators, EventParticipants, Sport, SportSkillLevel
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from datetime import datetime, timezone

class ParticipationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None

        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}
        dog_info = {'identifier': 'dog',
                    'password': 'barkbark', 'email': 'dog@bark.com'}
        sheep_info = {'identifier': 'sheep',
                    'password': 'baabaa', 'email': 'sheep@baa.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)
        self.dog_user = create_mock_user(dog_info)
        self.sheep_user = create_mock_user(sheep_info)


        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)
        self.dog_token, _ = Token.objects.get_or_create(user=self.dog_user)
        self.sheep_token, _ = Token.objects.get_or_create(user=self.sheep_user)


        authenticate(identifier=self.lion_user.identifier,
                     password=self.lion_user.password)
        authenticate(identifier=self.cat_user.identifier,
                     password=self.cat_user.password)
        authenticate(identifier=self.dog_user.identifier,
                     password=self.dog_user.password)
        authenticate(identifier=self.sheep_user.identifier,
                     password=self.sheep_user.password)

        event_data_1 = {
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": "2027-12-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.lion_user,
            "duration": 20
        }

        event_data_2 = {
            "name": "Basketball Time",
            "sport": "basketball",
            "startDate": "2027-09-18T15:00:00",
            "latitude": 56.002697,
            "longitude": 34.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 1,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 2,
            "acceptWithoutApproval": True,
            "organizer": self.cat_user,
            "duration": 34
        }

        event_data_3 = {
            "name": "Soccer Time 2",
            "sport": "soccer",
            "startDate": "2027-12-13T13:00:00",
            "latitude": 55.002697,
            "longitude": 55.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 1,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.lion_user,
            "duration": 45
        }

        event_data_4 = {
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": "2019-12-13T13:00:00",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.lion_user,
            "duration": 20
        }

        Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")

        SportSkillLevel.objects.get_or_create(user=self.lion_user, sport_id="soccer", skill_level=2)
        SportSkillLevel.objects.get_or_create(user=self.lion_user, sport_id="basketball", skill_level=5)
        SportSkillLevel.objects.get_or_create(user=self.cat_user, sport_id="soccer", skill_level=2)
        SportSkillLevel.objects.get_or_create(user=self.cat_user, sport_id="basketball", skill_level=2)
        SportSkillLevel.objects.get_or_create(user=self.dog_user, sport_id="soccer", skill_level=2)
        SportSkillLevel.objects.get_or_create(user=self.dog_user, sport_id="basketball", skill_level=2)

        self.event_with_approval = Event.objects.get(event_id = Event.create_event(event_data_1)['@id'])
        self.event_without_approval = Event.objects.get(event_id=Event.create_event(event_data_2)['@id'])
        self.event_3 = Event.objects.get(event_id=Event.create_event(event_data_3)['@id'])
        self.event_4 = Event.objects.get(event_id=Event.create_event(event_data_4)['@id'])

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        EventParticipants.objects.create(event = self.event_with_approval, user = self.dog_user, accepted_on = dt)
        EventSpectators.objects.create(event = self.event_3, user=self.dog_user, requested_on = dt)
        EventSpectators.objects.create(event=self.event_without_approval, user=self.dog_user, requested_on=dt)
        EventParticipationRequesters.objects.create(event = self.event_with_approval, user = self.dog_user, requested_on = dt, message = "Please accept, I really like this sport.")
        EventParticipationRequesters.objects.create(event = self.event_with_approval, user = self.cat_user, requested_on = dt)
        EventParticipationRequesters.objects.create(event = self.event_with_approval, user = self.sheep_user, requested_on = dt)
        

        self.request_param = {'already_participating': self.event_with_approval.event_id,
                              'already_spectator': self.event_without_approval.event_id,
                              'full_spectator': self.event_3.event_id,
                              'spectator_for_participating': self.event_with_approval.event_id,
                              'wrong_event_id': self.event_with_approval.event_id + self.event_without_approval.event_id + self.event_3.event_id,

                              'send_interest_success': self.event_with_approval.event_id,
                              'send_spectator_success': self.event_without_approval.event_id,
                              'participate_success': self.event_without_approval.event_id,

                              'delete_interest': self.event_with_approval.event_id,
                              'delete_spectator': self.event_3.event_id,
                              'delete_participating': self.event_with_approval.event_id,
                              'accept_reject_participants': self.event_with_approval.event_id,
                              'wrong_skill_level': self.event_without_approval.event_id,
                              'no_skill_level': self.event_without_approval.event_id,
                              'passed_event_interest': self.event_4.event_id,
                              'passed_event_spectator': self.event_4.event_id,
                              'passed_event_participant': self.event_4.event_id,
                              }

        self.request_token = {'already_participating': self.dog_token,
                              'already_spectator': self.dog_token,
                              'full_spectator': self.cat_token,
                              'spectator_for_participating': self.dog_token,
                              'wrong_event_id': self.cat_token,
                              'send_interest_success': self.lion_token,
                              'send_spectator_success': self.cat_token,
                              'participate_success': self.cat_token,
                              'delete_interest': self.cat_token,
                              'delete_spectator': self.dog_token,
                              'delete_participating': self.dog_token,
                              'accept_reject_participants': self.lion_token,
                              'wrong_skill_level': self.lion_token,
                              'no_skill_level': self.sheep_token,
                              'passed_event_interest': self.lion_token,
                              'passed_event_spectator': self.cat_token,
                              'passed_event_participant': self.lion_token,
                              }

        self.response_bodies = {'already_participating': {"message": "Already participating the event."},
                                'passed_event_interest': {"message": "Event start time is passed."},
                                'passed_event_spectator': {"message": "Event start time is passed."},
                                'passed_event_participant': {"message": "Event start time is passed."},
                                'already_spectator': {"message": "Already a spectator for the event."},
                                'full_spectator': {"message": "Added as spectator but spectator capacity is full."},
                                'spectator_for_participating': {"message": "Registered as participant to this event, if being spectator is wanted, remove participating status."},
                                'wrong_event_id': {"message": "Try with a valid event."},
                                'accept_reject_participants': {
                                    "@context": "https://www.w3.org/ns/activitystreams",
                                    "summary": f"{self.lion_user.identifier} accepted and rejected users to '{self.event_with_approval.name}' event",
                                    "type": "Collection",
                                    "items": [
                                        {
                                            "@context": "https://www.w3.org/ns/activitystreams",
                                            "summary": f"{self.lion_user.identifier} accepted {self.cat_user.identifier} to event '{self.event_with_approval.name}'.",
                                            "type": "Accept",
                                            "actor": {
                                                "type": "https://schema.org/Person",
                                                "@id": self.lion_user.user_id,
                                                "identifier": self.lion_user.identifier
                                            },
                                            "object": {
                                                "type": "RequestToParticipate",
                                                "actor": {
                                                    "type": "https://schema.org/Person",
                                                    "@id": self.cat_user.user_id,
                                                    "identifier": self.cat_user.identifier
                                                },
                                                "object": {
                                                    "type": "https://schema.org/SportsEvent",
                                                    "@id": self.event_with_approval.event_id
                                                }
                                            }
                                        },
                                        {
                                            "@context": "https://www.w3.org/ns/activitystreams",
                                            "summary": f"{self.lion_user.identifier} rejected {self.sheep_user.identifier}'s request to join the event '{self.event_with_approval.name}'.",
                                            "type": "Reject",
                                            "actor": {
                                                "type": "https://schema.org/Person",
                                                "@id": self.lion_user.user_id,
                                                "identifier": self.lion_user.identifier
                                            },
                                            "object": {
                                                "type": "RequestToParticipate",
                                                "actor": {
                                                    "type": "https://schema.org/Person",
                                                    "@id": self.sheep_user.user_id,
                                                    "identifier": self.sheep_user.identifier,
                                                },
                                                "object": {
                                                    "type": "https://schema.org/SportsEvent",
                                                    "@id": self.event_with_approval.event_id
                                                }
                                            }
                                        }
                                    ],
                                    "total_items": 2
                                },
                                'wrong_skill_level': {"message": "User skill level does not match the requirements for the event."},
                                'no_skill_level': {"message": "No skill level is entered for the sport."},

                            }

        

    def test_already_participating(self):
        test_type = 'already_participating'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_already_spectator(self):
        test_type = 'already_spectator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_full_spectator(self):
        test_type = 'full_spectator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertTrue(EventSpectators.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())

    def test_spectator_for_participating(self):
        test_type = 'spectator_for_participating'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_wrong_event_id(self):
        test_type = 'wrong_event_id'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_send_interest_success(self):
        test_type = 'send_interest_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EventParticipationRequesters.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())

    def test_send_spectator_success(self):
        test_type = 'send_spectator_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EventSpectators.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())

    def test_participate_success(self):
        test_type = 'participate_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EventParticipants.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())

    def test_delete_interest(self):
        test_type = 'delete_interest'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EventParticipationRequesters.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())
    
    def test_delete_spectator(self):
        test_type = 'delete_spectator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EventSpectators.objects.filter(
            event=request_param, user=self.dog_user.user_id).exists())

    def test_delete_participating(self):
        test_type = 'delete_participating'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/participants"

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EventParticipants.objects.filter(
            event=request_param, user=self.dog_user.user_id).exists())

    def test_accept_reject_participants(self):
        test_type = 'accept_reject_participants'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/participants"

        request_body = {
            "accept_user_id_list": [self.sheep_user.user_id + 1, self.cat_user.user_id],
            "reject_user_id_list": [45, self.sheep_user.user_id, 90, 132]
        }

        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertTrue(EventParticipants.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())
        self.assertFalse(EventParticipationRequesters.objects.filter(
            event=request_param, user=self.cat_user.user_id).exists())
        self.assertFalse(EventParticipationRequesters.objects.filter(
            event=request_param, user=self.sheep_user.user_id).exists())
        self.assertFalse(EventParticipants.objects.filter(
            event=request_param, user=self.sheep_user.user_id).exists())

    def test_no_skill_level(self):
        test_type = 'no_skill_level'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_wrong_skill_level(self):
        test_type = 'wrong_skill_level'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_passed_event_interest(self):
        test_type = 'passed_event_interest'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/interesteds"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_passed_event_participant(self):
        test_type = 'passed_event_participant'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/participants"

        request_body = {
            "accept_user_id_list": [self.sheep_user.user_id + 1, self.cat_user.user_id],
            "reject_user_id_list": [45, self.sheep_user.user_id, 90, 132]
        }

        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_passed_event_spectator(self):
        test_type = 'passed_event_spectator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/spectators"

        response = self.client.post(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
