import unittest
import requests
from ..api import event
from ...main import app

class TestEventAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_events_getall(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.get('/api/v1.0/events')
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')

    def test_events_filter_by_name(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.get('/api/v1.0/events?name=street')
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')

    def test_events_filter_by_sport(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.get('/api/v1.0/events?sport=103')
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')

    def test_events_filter_by_date_from(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.get('/api/v1.0/events?date_from=2021-06-05T16:00')
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')

    def test_events_filter_by_date_to(self):

        # Foreign key error
        # Adding without an error
        # without required fields
        # 
        response = self.app.get('/api/v1.0/events?date_to=2021-06-06T21:00')
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')


