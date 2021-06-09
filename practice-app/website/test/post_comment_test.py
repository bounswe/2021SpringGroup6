import unittest
import requests, json
from ..api.event import check_comment_has_text

class TestEventAPI(unittest.TestCase):

    # given an empty comment, it returns false
    def test_comment_empty(self):
        comment = ""
        result = check_comment_has_text(comment)
        self.assertEqual(result, False)

    # given any comment that has text, it returns true
    def test_comment_has_text(self):
        comment = "When does the event start?"
        result = check_comment_has_text(comment)
        self.assertEqual(result, True)
