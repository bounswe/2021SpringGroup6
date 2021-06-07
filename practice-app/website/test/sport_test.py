import unittest
from ..api.sport import get_sport_by_keyword
from ..models import Sport


class TestSportAPI(unittest.TestCase):

    def setUp(self):
        # mock data
        self.data = [Sport(id = 102, sport = "Football"), Sport(id = 103, sport = "Basketball"), Sport(id = 105, sport = "Tennis")]        

    # Test with keyword "ball"
    def test_sport_keyword(self):

        ball_keyword = get_sport_by_keyword(self.data, "ball")
        expected = [self.data[0], self.data[1]] # Only "Football" and "Basketball"

        self.assertEqual(ball_keyword, expected)

    # Test with no keyword
    def test_no_keyword(self):
        
        no_keyword = get_sport_by_keyword(self.data, "")
        expected = self.data # No filtering

        self.assertEqual(no_keyword, expected)
    
    # Test with no result, no sport with "aa"
    def test_no_result(self):

        no_data = get_sport_by_keyword(self.data, "aa")
        expected = [] # No match

        self.assertEqual(no_data, expected)


