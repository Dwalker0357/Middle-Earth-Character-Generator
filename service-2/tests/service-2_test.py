import unittest
from application import app
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests



# Setting up our parent test class which is itself a child of another class (TestCase)
class TestBase(TestCase):
    def create_app(self):
        return app



# This test is checking that if a random value(1) is used to select a corresponding entry in a list of strings(Race)
# the resulting output will be "Woodland Elf" which is the second entry in the list because of pythons zero based indexing 
class Test_Service_2(TestBase):
    def test_Race(self):
        with patch("random.randrange") as r:
            r.return_value = 1
            response = self.client.get(url_for("Race"))
            self.assertIn(b"Woodland Elf", response.data)



# This test is checking that if a random value(2) is used to select a corresponding entry in a list of strings(Stature)
# the resulting output will be "Average" which is the third entry in the list because of pythons zero based indexing 
    def test_Stature(self):
        with patch("random.randrange") as r:
            r.return_value = 2
            response = self.client.get(url_for("Stature"))
            self.assertIn(b"Average", response.data)



# This test is checking that if a random value(3) is used to select a corresponding entry in a list of strings(Location)
# the resulting output will be "Helm's Deep" which is the fourth entry in the list because of pythons zero based indexing 
    def test_Location(self):
        with patch("random.randrange") as r:
            r.return_value = 3
            response = self.client.get(url_for("Location"))
            self.assertIn(b"Helm's Deep", response.data)



# This test is checking that if a random value(4) is used to select a corresponding entry in a list of strings(Rank)
# the resulting output will be "Master" which is the fifth entry in the list because of pythons zero based indexing 
    def test_Rank(self):
        with patch("random.randrange") as r:
            r.return_value = 4
            response = self.client.get(url_for("Rank"))
            self.assertIn(b"Master", response.data)



# This test is checking that if a random value(10) is used to select a corresponding entry in a list of strings(Profession)
# the resulting output will be "Mercenary" which is the eleventh entry in the list because of pythons zero based indexing 
    def test_Profession(self):
        with patch("random.randrange") as r:
            r.return_value = 10
            response = self.client.get(url_for("Profession"))
            self.assertIn(b"Mercenary", response.data)