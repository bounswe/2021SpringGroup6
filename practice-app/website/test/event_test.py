import unittest
from ..api.event import check_event_date, check_event_sport
from ..models import Event

class TestEventAPI(unittest.TestCase):

    def test_date_correct_format(self):
        """
            Given a string with correct format as YYYY-MM-DD, returns True
        """
        event = Event(date = "2021-12-30T12:30")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, True)


    def test_date_invalid_month(self):
        """
            Given a string with a non existing month such as 13 returns False
        """
        event = Event(date="2021-13-30T12:30")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, False)

    def test_date_invalid_day(self):
        """
            Given a string with a non existing day such as 45 returns False
        """
        event = Event(date="2021-10-45T12:30")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, False)


    def test_date_invalid_hour(self):
        """
            Given a string with a non existing hour such as 25 returns False
        """
        event = Event(date = "2021-11-30T25:30")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, False)

    def test_date_invalid_minute(self):
        """
            Given a string with a non existing minute such as 61 returns False
        """
        event = Event(date = "2021-11-30T23:61")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, False)


    def test_date_invalid_format(self):
        """
            Given a string with a different format returns False
        """
        event = Event(date = "2021-11-30")

        is_date_correct = check_event_date(event)

        self.assertEqual(is_date_correct, False)


    def test_sport_correct(self):
        """
            Given sport id between 102-120 returns True
        """
        event = Event(sport = "104")

        is_sport_correct = check_event_sport(event)

        self.assertEqual(is_sport_correct, True)

    def test_sport_out_of_range(self):
        """
            Given sport id not between 102-120 returns False
        """
        event = Event(sport = "5")

        is_sport_correct = check_event_sport(event)

        self.assertEqual(is_sport_correct, False)

    def test_sport_integer(self):
        """
            Given sport id not between 102-120 returns False
        """
        event = Event(sport = 103)

        is_sport_correct = check_event_sport(event)

        self.assertEqual(is_sport_correct, True)

    def test_sport_incorrect_type(self):
        """
            Given sport id as a string that can be changed to a integer returns False
        """
        event = Event(sport = "five")

        is_sport_correct = check_event_sport(event)


        self.assertEqual(is_sport_correct, False)
