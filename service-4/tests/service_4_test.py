import unittest
from application import app
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests



class TestBase(TestCase):
    def create_app(self):
        return app



# This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Melee_Prowess)
# the resulting output will be "0" which is the second entry in the list because of pythons zero based indexing
class Test_Service_4(TestBase):
    def test_Melee_Prowess(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Melee_Prowess"))
            self.assertIn(b"0", response.data)
            

    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Archery_Prowess)
    # the resulting output will be "0" which is the third entry in the list because of pythons zero based indexing
    def test_Archery_Prowess(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Archery_Prowess"))
            self.assertIn(b"0", response.data)



    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Strength)
    # the resulting output will be "0" which is the fourth entry in the list because of pythons zero based indexing
    def test_Strength(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Strength"))
            self.assertIn(b"0", response.data)



    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Endurance)
    # the resulting output will be "0" which is the fith entry in the list because of pythons zero based indexing
    def test_Endurance(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Endurance"))
            self.assertIn(b"0", response.data)



    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Intelligence)
    # the resulting output will be "0" which is the sixth entry in the list because of pythons zero based indexing
    def test_Intelligence(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Intelligence"))
            self.assertIn(b"0", response.data)

    

    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Awareness)
    # the resulting output will be "0" which is the seventh entry in the list because of pythons zero based indexing
    def test_Awareness(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Awareness"))
            self.assertIn(b"0", response.data)
   


    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Dexterity)
    # the resulting output will be "0" which is the eighth entry in the list because of pythons zero based indexing
    def test_Dexterity(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Dexterity"))
            self.assertIn(b"0", response.data)


    
    # This test is checking that if a random value(0) is used to select a corresponding entry in a list of strings(Dodge)
    # the resulting output will be "0" which is the ninth entry in the list because of pythons zero based indexing
    def test_Dodge(self):
        with patch("random.randrange") as r:
            r.return_value = 0
            response = self.client.get(url_for("Dodge"))
            self.assertIn(b"0", response.data)