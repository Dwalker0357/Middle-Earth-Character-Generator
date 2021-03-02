import unittest
from application import app
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests



class TestBase(TestCase):
    def create_app(self):
        return app



# This test is checking that if a random value(1) is used to select a corresponding entry in a list of strings(Melee_Prowess)
# the resulting output will be "1" which is the second entry in the list because of pythons zero based indexing
class Test_Service_4(TestBase):
    def test_Melee_Prowess(self):
        with patch("random.randrange") as r:
            r.return_value = 1
            response = self.client.get(url_for("Melee_Prowess"))
            self.assertIn(b"1", response.data)
            

    # This test is checking that if a random value(2) is used to select a corresponding entry in a list of strings(Archery_Prowess)
    # the resulting output will be "2" which is the third entry in the list because of pythons zero based indexing
    def test_Archery_Prowess(self):
        with patch("random.randrange") as r:
            r.return_value = 2
            response = self.client.get(url_for("Archery_Prowess"))
            self.assertIn(b"2", response.data)



    # This test is checking that if a random value(3) is used to select a corresponding entry in a list of strings(Strength)
    # the resulting output will be "3" which is the fourth entry in the list because of pythons zero based indexing
    def test_Strength(self):
        with patch("random.randrange") as r:
            r.return_value = 3
            response = self.client.get(url_for("Strength"))
            self.assertIn(b"3", response.data)



    # This test is checking that if a random value(4) is used to select a corresponding entry in a list of strings(Endurance)
    # the resulting output will be "4" which is the fith entry in the list because of pythons zero based indexing
    def test_Endurance(self):
        with patch("random.randrange") as r:
            r.return_value = 4
            response = self.client.get(url_for("Endurance"))
            self.assertIn(b"4", response.data)



    # This test is checking that if a random value(5) is used to select a corresponding entry in a list of strings(Intelligence)
    # the resulting output will be "5" which is the sixth entry in the list because of pythons zero based indexing
    def test_Intelligence(self):
        with patch("random.randrange") as r:
            r.return_value = 5
            response = self.client.get(url_for("Intelligence"))
            self.assertIn(b"5", response.data)

    

    # This test is checking that if a random value(6) is used to select a corresponding entry in a list of strings(Awareness)
    # the resulting output will be "6" which is the seventh entry in the list because of pythons zero based indexing
    def test_Awareness(self):
        with patch("random.randrange") as r:
            r.return_value = 6
            response = self.client.get(url_for("Awareness"))
            self.assertIn(b"6", response.data)
   


    # This test is checking that if a random value(7) is used to select a corresponding entry in a list of strings(Dexterity)
    # the resulting output will be "7" which is the eighth entry in the list because of pythons zero based indexing
    def test_Dexterity(self):
        with patch("random.randrange") as r:
            r.return_value = 7
            response = self.client.get(url_for("Dexterity"))
            self.assertIn(b"7", response.data)


    
    # This test is checking that if a random value(8) is used to select a corresponding entry in a list of strings(Dodge)
    # the resulting output will be "8" which is the ninth entry in the list because of pythons zero based indexing
    def test_Dodge(self):
        with patch("random.randrange") as r:
            r.return_value = 8
            response = self.client.get(url_for("Dodge"))
            self.assertIn(b"8", response.data)