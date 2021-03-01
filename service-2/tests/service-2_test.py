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



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Race)
# the resulting output will be "Orc" which is the second entry in the list because of pythons zero based indexing 
class Test_Service_2(TestBase):
    def test_Race(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Race"))
            self.assertIn(b"Orc", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Stature)
# the resulting output will be "Tiny" which is the third entry in the list because of pythons zero based indexing 
    def test_Stature(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Stature"))
            self.assertIn(b"Tiny", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Location)
# the resulting output will be "The Shire" which is the fourth entry in the list because of pythons zero based indexing 
    def test_Location(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Location"))
            self.assertIn(b"The Shire", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Rank)
# the resulting output will be "Novice" which is the fifth entry in the list because of pythons zero based indexing 
    def test_Rank(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Rank"))
            self.assertIn(b"Novice", response.data)



# This test is checking that if a random value(10) is used to select a corresponding entry in a list of strings(Profession)
# the resulting output will be "FootSoldier" which is the eleventh entry in the list because of pythons zero based indexing 
    def test_Profession(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Profession"))
            self.assertIn(b"FootSoldier", response.data)