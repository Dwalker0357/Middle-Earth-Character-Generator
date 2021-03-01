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


# This test is checking that if a random value(1) is used to select a corresponding entry in a list of strings(Grade)
# the resulting output will be "Rusty" which is the second entry in the list because of pythons zero based indexing 
class Test_Service_3(TestBase):
    def test_Grade(self):
        with patch("random.randrange") as r:
            r.return_value = 1
            response = self.client.get(url_for("Grade"))
            self.assertIn(b"Rusty", response.data)



# This test is checking that if a random value(2) is used to select a corresponding entry in a list of strings(Weapon)
# the resulting output will be "ShortSword" which is the third entry in the list because of pythons zero based indexing 
    def test_Weapon(self):
        with patch("random.randrange") as r:
            r.return_value = 2
            response = self.client.get(url_for("Weapon"))
            self.assertIn(b"ShortSword", response.data)



# This test is checking that if a random value(3) is used to select a corresponding entry in a list of strings(Stance)
# the resulting output will be "Rock Solid" which is the forth entry in the list because of pythons zero based indexing 
    def test_Stance(self):
        with patch("random.randrange") as r:
            r.return_value = 3
            response = self.client.get(url_for("Stance"))
            self.assertIn(b"Rock Solid", response.data)



# This test is checking that if a random value(4) is used to select a corresponding entry in a list of strings(Trait_1)
# the resulting output will be "Massive Natural Biceps" fifth is the secound entry in the list because of pythons zero based indexing 
    def test_Trait_1(self):
        with patch("random.randrange") as r:
            r.return_value = 4
            response = self.client.get(url_for("Trait_1"))
            self.assertIn(b"Massive Natural Biceps", response.data)



# This test is checking that if a random value(5) is used to select a corresponding entry in a list of strings(Trait_2)
# the resulting output will be "Hobbit Hater" which is the sixth entry in the list because of pythons zero based indexing 
    def test_Trait_2(self):
        with patch("random.randrange") as r:
            r.return_value = 5
            response = self.client.get(url_for("Trait_2"))
            self.assertIn(b"Hobbit Hater", response.data)



# This test is checking that if a random value(15) is used to select a corresponding entry in a list of strings(Trait_3)
# the resulting output will be "Snapped Up" which is the sixteenth entry in the list because of pythons zero based indexing 
    def test_Trait_3(self):
        with patch("random.randrange") as r:
            r.return_value = 15
            response = self.client.get(url_for("Trait_3"))
            self.assertIn(b"Snapped Up", response.data)

