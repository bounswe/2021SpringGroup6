import unittest
from ..api.event import check_event_id, check_weather_icon
from ..models import Event

class TestEventAPI(unittest.TestCase):

    def test_valid_event_id(self):
        """
            Check if the event id is valid, i.e id is larger than 0
        """
        event = Event(id = 51)
        is_id_valid = check_event_id(event)
        self.assertEqual(is_id_valid , True)
    
    
    def test_invalid_event_id(self):  
        """
            Check if the event id is invalid, i.e id is smaller than 1
        """
        event = Event(id = -15)
        is_id_valid = check_event_id(event)
        self.assertEqual(is_id_valid , False)
 
   
    def test_valid_weather_icon_id(self):  
        """
            Check if the weather icon id is valid
        """
        weather_icon_id = "03d"
        is_weather_icon_valid = check_weather_icon(weather_icon_id)
        self.assertEqual(is_weather_icon_valid , True)
   
   
    def test_invalid_weather_icon_id(self):
        """
            Check if the weather icon id is invalid
        """
        weather_icon_id = "07x"
        is_weather_icon_valid = check_weather_icon(weather_icon_id)
        self.assertEqual(is_weather_icon_valid , False)



    
    

  