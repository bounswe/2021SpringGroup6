import datetime
from django.test import Client, TestCase
from ..models.activity_stream_models import ActivityStream
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user


class GetActivityStreamTest(TestCase):

    def setUp(self):
        self.client = Client()

        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)
        self.token, _ = Token.objects.get_or_create(user=self.lion_user)
        utc_dt = datetime.datetime.now(datetime.timezone.utc)  
        dt = utc_dt.astimezone()
        block=ActivityStream.objects.create(type='Block',actor=self.lion_user, object=self.cat_user, date=dt)
        utc_dt = datetime.datetime.now(datetime.timezone.utc) 
        dt = utc_dt.astimezone()
        follow=ActivityStream.objects.create(type='Follow',actor=self.cat_user, object=self.lion_user, date=dt)
        self.path = "/activitystream?limit=2"

        self.response_body = {
                "@context": "https://www.w3.org/ns/activitystreams",
                "summary": "Activity stream",
                "type": "OrderedCollection",
                "total_items": 2,
                "orderedItems":[
                    {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": f"{self.cat_user.identifier} followed {self.lion_user.identifier}",
                    "id": follow.id,
                    "type": "Follow",
                    "actor": {
                        "type": "https://schema.org/Person", 
                        "@id": self.cat_user.user_id,
                        "identifier": self.cat_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person", 
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    }
                    },
                    {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": f"{self.lion_user.identifier} blocked {self.cat_user.identifier}",
                    "id": block.id,
                    "type": "Block",
                    "actor": {
                        "type": "https://schema.org/Person", 
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person", 
                        "@id": self.cat_user.user_id,
                        "identifier": self.cat_user.identifier
                    },
                    }

                ]
        }

    def test_not_authorized(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'User not logged in.')

    def test_get_activity_stream(self):
        response = self.client.get(
            self.path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_body)
