from django.test import Client, TestCase
from ..models import Block
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user


class GetBlockedTest(TestCase):

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

        self.token, _ = Token.objects.get_or_create(user=self.lion_user)

        Block.objects.create(blocker=self.lion_user, blocked=self.cat_user)
        Block.objects.create(blocker=self.lion_user, blocked=self.dog_user)

        self.path = "/users/" + str(self.lion_user.user_id) + "/blocked"

        self.response_body = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "lion's blocking activities.",
            "type": "Collection",
            "total_items": 2,
            "items": [
                {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": "lion blocked cat",
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
                    }
                },
                {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": "lion blocked dog",
                    "type": "Block",
                    "actor": {
                        "type": "https://schema.org/Person",
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person",
                        "@id": self.dog_user.user_id,
                        "identifier": self.dog_user.identifier
                    }
                },
            ]
        }

    def test_get_following(self):
        response = self.client.get(
            self.path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_body)
