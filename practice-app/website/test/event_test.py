import unittest
import requests, json


class TestEventAPI(unittest.TestCase):

    def setUp(self):
        self.req = "http://127.0.0.1:5000/api/v1.0/events"
        self.headers = {'Content-type': 'application/json'}

    def test_events_POST_no_user(self):

        # No user with id -1
        event ={
            'name': 'Footbal Match', 
            'date': '11.05.2021T12:30',
            'location': 'Trabzon',
            'creator_user': '-1',
            'sport': '103'
        }
        response = requests.post(self.req, data=json.dumps(event), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_events_POST_no_without_required(self):

        # Date field is missing
        event ={
            'name': 'Footbal Match', 
            'location': 'Trabzon',
            'creator_user': '1',
            'sport': '103'
        }
        response = requests.post(self.req, data=json.dumps(event), headers=self.headers)
        self.assertEqual(response.status_code, 400)
    
    def test_events_POST_invalid_address(self):

        # Address is not correct
        event ={
            'name': 'Footbal Match', 
            'date': '11.05.2021T12:30',
            'location': 'aswegaerhqerhjerfasdv<',
            'creator_user': '1',
            'sport': '103'
        }
        response = requests.post(self.req, data=json.dumps(event), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_events_POST_invalid_sport_id(self):

        # Sport ids between 102-120
        event ={
            'name': 'Footbal Match', 
            'date': '11.05.2021T12:30',
            'location': 'd',
            'creator_user': '-1',
            'sport': '103'
        }
        response = requests.post(self.req, data=json.dumps(event), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_events_POST_invalid_date_format(self):

        # Date format: YYYY-MM-DDTHH.MM
        event ={
            'name': 'Footbal Match', 
            'date': '11.05.2021',
            'location': 'd',
            'creator_user': '-1',
            'sport': '103'
        }
        response = requests.post(self.req, data=json.dumps(event), headers=self.headers)
        self.assertEqual(response.status_code, 400)




class TestDiscussionForEvent(unittest.TestCase):


    def test_GET_1(self):
        # For nonexisting event
        response = requests.get('http://127.0.0.1:5000/api/v1.0/events/1115/discussions')
        self.assertEqual(response.status_code, 500)


    def test_GET_2(self):
        # For an existing event
        response = requests.get('http://127.0.0.1:5000/api/v1.0/events/1/discussions')
        self.assertEqual(response.status_code, 201)


