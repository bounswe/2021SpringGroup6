import unittest
import requests, json

class TestAuthAPI(unittest.TestCase):

    def setUp(self):
        # self.req = "http://127.0.0.1:5000/api/v1.0/users"
        self.headers = {'Content-type': 'application/json'}

    def test_user_POST(self):

        # Equipment named Ball
        User ={
            'name': 'Omer'
        }
        response = requests.post(self.req, data=json.dumps(User), headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_user_POST_empty_name(self):

        # Name field is missing
        User ={
            'name': ''
        }

        response = requests.post(self.req, data=json.dumps(User), headers=self.headers)
        self.assertEqual(response.status_code, 201)