import unittest
import requests, json


# Checks the number of messages sent in the discussion
def hasMoreThan2Messages(messages):
    return len(messages) > 2

class TestHasMoreThan2Messages(unittest.TestCase):

    def test_1(self):
        # For no discussion case
        messages = []
        result = hasMoreThan2Messages(messages)
        self.assertEqual(result, False)

    def test_2(self):
        # For 2 messages
        messages = ['Hello how are you?', 'Fine thanks, and you?']
        result = hasMoreThan2Messages(messages)
        self.assertEqual(result, False)
    
    def test_3(self):
        # For 3 messages
        messages = ['Hello how are you?', 'Fine thanks, and you?', 'Good']
        result = hasMoreThan2Messages(messages)
        self.assertEqual(result, True)


# Checks if at least one of the people is mentioned in the
# discussion or not
def hasReferenceToName(messages, namesOfPeople):
    for i in range(len(messages)):
        for j in range(len(namesOfPeople)):
            if namesOfPeople[j].lower() in messages[i].lower():
                return True
    return False


class TestHasReferenceToName(unittest.TestCase):

    def test_1(self):
        # For not mentioned case
        messages = ['How are you today?', 'I am very happy']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = hasReferenceToName(messages, namesOfPeople)
        self.assertEqual(result, False)

    def test_2(self):
        # For mentioned with the first letter as capital case
        messages = ['Hello how are you Ayse?', 'Fine thanks, and you?', 'Thanks I am fine', 'Good']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = hasReferenceToName(messages, namesOfPeople)
        self.assertEqual(result, True)
    
    def test_3(self):
        # For mentioned with the all letters as capital case
        messages = ['Hello how are you OSMAN?', 'Fine thanks, and you?']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = hasReferenceToName(messages, namesOfPeople)
        self.assertEqual(result, True)
    
    def test_4(self):
        # For mentioned without any capital letter case
        messages = ['Hello how are you?', 'Fine thanks, and you frank?', 'Thanks I am fine', 'Good']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman', 'Frank']

        result = hasReferenceToName(messages, namesOfPeople)
        self.assertEqual(result, True)


# If an event has more than 3 messages in discussions
# or a person is referenced by name in one of the messages,
# the event is special. The function isn't case sensitive.
def areDiscussionsForEventSpecial(messages, namesOfPeople):
    return hasMoreThan2Messages(messages) or hasReferenceToName(messages, namesOfPeople)


class TestAreDiscussionsForEventSpecial(unittest.TestCase):

    def test_1(self):
        # For no discussion case
        messages = []
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = areDiscussionsForEventSpecial(messages, namesOfPeople)
        self.assertEqual(result, False)

    def test_2(self):
        # For more than 2 discussions without referencing
        messages = ['Hello how are you?', 'Fine thanks, and you?', 'Thanks I am fine', 'Good']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = areDiscussionsForEventSpecial(messages, namesOfPeople)
        self.assertEqual(result, True)
   
    def test_3(self):
        # For less than 3 discussions, but with referencing
        messages = ['Hello how are you OSMAN?', 'Fine thanks, and you?']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = areDiscussionsForEventSpecial(messages, namesOfPeople)
        self.assertEqual(result, True)
    
    def test_4(self):
        # For no discussion case
        messages = ['Hello how are you Ahmet?', 'Fine thanks, and you?', 'Thanks I am fine', 'Good']
        namesOfPeople = ['Ayse', 'Ahmet', 'Hasan', 'Osman']

        result = areDiscussionsForEventSpecial(messages, namesOfPeople)
        self.assertEqual(result, True)


   
