import unittest
import requests
from ..api import event
from ...main import app

class TestEventAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_events_POST(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.post('/api/v1.0/events', json={
            'name': '', 
            'date': '',
            'location': '',
            'creator_user': '',
        })
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')
