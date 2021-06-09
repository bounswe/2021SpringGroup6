import unittest
from ..api.sport import get_sport_by_keyword
from ..models import Sport


class TestSportAPI(unittest.TestCase):

    def setUp(self):
        # mock data
        self.data = [Sport(id = 102, sport = "Football"), Sport(id = 103, sport = "Basketball"), Sport(id = 105, sport = "Tennis")]        

    def test_sport_keyword(self):
        """
            Given keyword "ball", sports that contain that keyword should be returned.
        """

        ball_keyword = get_sport_by_keyword(self.data, "ball")
        expected = [self.data[0], self.data[1]] # Only "Football" and "Basketball"

        self.assertEqual(ball_keyword, expected)

    def test_no_keyword(self):
        """
            Given no keyword, all sports should be returned.
        """
        no_keyword = get_sport_by_keyword(self.data, "")
        expected = self.data # No filtering

        self.assertEqual(no_keyword, expected)
    
    def test_no_result(self):
        """
            Given a keyword not existing on sports, no sport should be returned.
        """

        no_data = get_sport_by_keyword(self.data, "aa")
        expected = [] # No match

        self.assertEqual(no_data, expected)


