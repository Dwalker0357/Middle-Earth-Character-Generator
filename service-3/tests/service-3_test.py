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


# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Grade)
# the resulting output will be "Broken" which is the second entry in the list because of pythons zero based indexing 
class Test_Service_3(TestBase):
    def test_Grade(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Grade"))
            self.assertIn(b"Broken", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Weapon)
# the resulting output will be "Barefist" which is the third entry in the list because of pythons zero based indexing 
    def test_Weapon(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Weapon"))
            self.assertIn(b"Barefist", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Stance)
# the resulting output will be "Clumsy" which is the forth entry in the list because of pythons zero based indexing 
    def test_Stance(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Stance"))
            self.assertIn(b"Clumsy", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Trait_1)
# the resulting output will be "Odin Force Disease Resist" fifth is the secound entry in the list because of pythons zero based indexing 
    def test_Trait_1(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Trait_1"))
            self.assertIn(b"Odin Force Disease Resist", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Trait_2)
# the resulting output will be "Orc Hate" which is the sixth entry in the list because of pythons zero based indexing 
    def test_Trait_2(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Trait_2"))
            self.assertIn(b"Orc Hate", response.data)



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Trait_3)
# the resulting output will be "Natural Sprinter" which is the sixteenth entry in the list because of pythons zero based indexing 
    def test_Trait_3(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Trait_3"))
            self.assertIn(b"Natural Sprinter", response.data)