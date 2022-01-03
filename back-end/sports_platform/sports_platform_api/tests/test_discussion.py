from django.test import Client, TestCase
from ..models import Event, EventSpectators, EventParticipants, DiscussionPost, DiscussionComment, Sport
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from datetime import datetime, timezone

class DiscussionTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None

        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}
        dog_info = {'identifier': 'dog',
                    'password': 'barkbark', 'email': 'dog@bark.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)
        self.dog_user = create_mock_user(dog_info)


        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)
        self.dog_token, _ = Token.objects.get_or_create(user=self.dog_user)


        authenticate(identifier=self.lion_user.identifier,
                     password=self.lion_user.password)
        authenticate(identifier=self.cat_user.identifier,
                     password=self.cat_user.password)
        authenticate(identifier=self.dog_user.identifier,
                     password=self.dog_user.password)

        event_data_1 = {
            "name": "Let's play soccer",
            "sport": "soccer",
            "startDate": "2021-12-13T13:00:00",
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
            "startDate": "2021-09-18T15:00:00",
            "latitude": 56.002697,
            "longitude": 34.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 1,
            "maxSpectatorCapacity": 2,
            "minSkillLevel": 1,
            "maxSkillLevel": 2,
            "acceptWithoutApproval": True,
            "organizer": self.lion_user,
            "duration": 34,
            "canEveryoneSeePosts": True,
            "canEveryonePostPosts": False,
        }

        event_data_3 = {
            "name": "Soccer Time 2",
            "sport": "soccer",
            "startDate": "2021-12-13T13:00:00",
            "latitude": 55.002697,
            "longitude": 55.716763,
            "minimumAttendeeCapacity": 1,
            "maximumAttendeeCapacity": 2,
            "maxSpectatorCapacity": 1,
            "minSkillLevel": 1,
            "maxSkillLevel": 3,
            "acceptWithoutApproval": False,
            "organizer": self.lion_user,
            "duration": 45,
            "canEveryoneSeePosts": False,
            "canEveryonePostPosts": False,
        }

        Sport.objects.create(name="soccer")
        Sport.objects.create(name="basketball")


        self.event_true_true = Event.objects.get(event_id = Event.create_event(event_data_1)['@id'])
        self.event_true_false = Event.objects.get(event_id=Event.create_event(event_data_2)['@id'])
        self.event_false_false = Event.objects.get(event_id=Event.create_event(event_data_3)['@id'])

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        EventParticipants.objects.create(event=self.event_false_false, user=self.dog_user, accepted_on=dt)
        EventSpectators.objects.create(event=self.event_true_false, user=self.dog_user, requested_on=dt)

        self.post1 = DiscussionPost.objects.create(event=self.event_true_true, author=self.cat_user, text="My First Post", dateCreated=dt)
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        self.post2 = DiscussionPost.objects.create(event=self.event_true_true, author=self.lion_user, text="My Second Post", dateCreated=dt)

        self.comment1 = DiscussionComment.objects.create(post=self.post1, author=self.dog_user, text="Comment To First Post", dateCreated=dt)
        
        self.post_body = {
            "sharedContent": "https://shorturl.at/vxHI3",
            "text" : "I added the photo of the field"
        }

        self.comment_body = {
            "text": "Field looks great"
        }

        self.request_param = {'cannot_see': self.event_false_false.event_id,
                              'cannot_post': self.event_true_false.event_id,
                              'post_success': self.event_true_true.event_id,
                              'comment_success': [self.event_true_true.event_id, self.post1.post_id ],
                              'delete_post_by_creator': [self.event_true_true.event_id, self.post1.post_id],
                              'delete_post_by_author': [self.event_true_true.event_id, self.post1.post_id],
                              'delete_comment': [self.event_true_true.event_id, self.post1.post_id, self.comment1.comment_id],
                              'cannot_delete': [self.event_true_true.event_id, self.post1.post_id, self.comment1.comment_id],
                              'get_posts': self.event_true_true.event_id,
                              'wrong_event_id': [self.event_true_false.event_id,self.post1.post_id]
                              }

        self.request_token = {'cannot_see': self.cat_token,
                              'cannot_post': self.cat_token,
                              'post_success': self.dog_token,
                              'comment_success': self.cat_token,
                              'delete_post_by_creator': self.lion_token,
                              'delete_post_by_author': self.cat_token,
                              'delete_comment': self.dog_token,
                              'cannot_delete': self.cat_token,
                              'get_posts': self.lion_token,
                              'wrong_event_id': self.lion_token,
                              }

        self.response_bodies = {'cannot_see': {"message": "Only participants and spectators can see posts."},
                                'cannot_post': {"message": "Only participants and spectators can post posts."},
                                'cannot_delete': {"message": "Only comment authors and event creators can delete posts."},
                                'wrong_event_id': {"message": "This post does not belong to that event_id."},
                                'get_posts': {
                                    "@context": "https://schema.org/SportsEvent",
                                    "@id": self.event_true_true.event_id,
                                    "additionalProperty": {
                                        "@type": "PropertyValue",
                                        "name": "posts",
                                        "value": [{
                                            "@context": "https://schema.org/SocialMediaPosting",
                                            "@id": self.post1.post_id,
                                            "author": {
                                                "@context": "https://schema.org/Person",
                                                "@id": self.post1.author.user_id,
                                                "identifier": self.post1.author.identifier
                                            },
                                            "text": self.post1.text,
                                            "dateCreated": self.post1.dateCreated,
                                            "comment":[
                                                {
                                                    "@context": "https://schema.org/Comment",
                                                    "@id": self.comment1.comment_id,
                                                    "author": {
                                                        "@context": "https://schema.org/Person",
                                                        "@id": self.comment1.author.user_id,
                                                        "identifier": self.comment1.author.identifier
                                                    },
                                                    "text": self.comment1.text,
                                                    "dateCreated": self.comment1.dateCreated,
                                                }
                                            ]
                                            },
                                            {
                                            "@context": "https://schema.org/SocialMediaPosting",
                                            "@id": self.post2.post_id,
                                            "author": {
                                                "@context": "https://schema.org/Person",
                                                "@id": self.post2.author.user_id,
                                                "identifier": self.post2.author.identifier
                                            },
                                            "text": self.post2.text,
                                            "dateCreated": self.post2.dateCreated,
                                            "comment": []
                                        }
                                            
                                        ]
                                    }
                                },
                            }

        
    def test_cannot_see(self):
        test_type = 'cannot_see'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/discussion"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)
    
    def test_cannot_post(self):
        test_type = 'cannot_post'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/discussion"

        response = self.client.post(
            path, self.post_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_post_success(self):
        test_type = 'post_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/discussion"

        response = self.client.post(
            path, self.post_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(DiscussionPost.objects.filter(
            event=self.event_true_true, author=self.dog_user.user_id).exists())

    def test_comment_success(self):
        test_type = 'comment_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param[0]) + "/discussion/" + str(request_param[1]) 

        response = self.client.post(
            path, self.comment_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(DiscussionComment.objects.filter(author=self.cat_user, post=self.post1).exists())

    def test_delete_post_by_creator(self):
        test_type = 'delete_post_by_creator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param[0]) + "/discussion/" + str(request_param[1]) 

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(DiscussionPost.objects.filter(post_id=self.post1.post_id).exists())

    def test_delete_post_by_author(self):
        test_type = 'delete_post_by_author'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + \
            str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(DiscussionPost.objects.filter(
            post_id=self.post1.post_id).exists())

    def test_delete_comment(self):
        test_type = 'delete_comment'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param[0]) + "/discussion/" + str(request_param[1]) + "/comment/" + str(request_param[2])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(DiscussionComment.objects.filter(
            comment_id=self.comment1.comment_id).exists())

    def test_cannot_delete(self):
        test_type = 'cannot_delete'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param[0]) + "/discussion/" + str(request_param[1]) + "/comment/" + str(request_param[2])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_get_posts(self):
        test_type = 'get_posts'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param) + "/discussion"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 200)

    def test_wrong_event_id(self):
        test_type = 'wrong_event_id'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/events/" + str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.post(
            path, self.post_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

