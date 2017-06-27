import unittest


import PhoneBook
import phonebookDB

class PhoneBookTests(unittest.TestCase):
    def setUp(self):
        """Create a phonebook object"""
        self.phoneBook1 = PhoneBook.PhoneBooks("brect","philips","0479354119")

    def test_creation(self):
        """Make sure phonebook is an instance of PhoneBooks"""
        self.assertIsInstance(self.phoneBook1,PhoneBook.PhoneBooks)




