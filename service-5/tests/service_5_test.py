import unittest
from application import app
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests




class TestBase(TestCase):
    def create_app(self):
        return app



# Object modification tests for Grade



# This test is checking that if "FoeHammer"(data) and the randomly generated object Grade(g) is not equal to  
# Eleven Mastercrafted then the function will make the outputting Grade equal to Eleven Mastercrafted which is then posted(p) to service-1.
class Test_Service_5_Grade(TestBase):
    def test_Grade_Foehammer(self):
        with patch("requests.get") as g:
            g.return_value.text = "Shoddy"
            with patch("requests.post") as p:
                 p.return_value.text = "Eleven Mastercrafted"
                 response = self.client.post(url_for('Grade'),data="FoeHammer")
                 self.assertIn(b"Eleven Mastercrafted", response.data)



    # This test is checking that if "Sting"(data) and the randomly generated object Grade(g) is not equal to  
    # Eleven Mastercrafted then the function will make the outputting Grade equal to Eleven Mastercrafted which is then posted(p) to service-1.
    def test_Grade_Sting(self):
        with patch("requests.get") as g:
            g.return_value.text = "Rusty"
            with patch("requests.post") as p:
                 p.return_value.text = "Eleven Mastercrafted"
                 response = self.client.post(url_for('Grade'),data="Sting")
                 self.assertIn(b"Eleven Mastercrafted", response.data)
    


    # This test is checking that if "Narsil"(data) and the randomly generated object Grade(g) is not equal to  
    # Eleven Mastercrafted then the function will make the outputting Grade equal to Eleven Mastercrafted which is then posted(p) to service-1.
    def test_Grade_Narsil(self):
        with patch("requests.get") as g:
            g.return_value.text = "Rusty"
            with patch("requests.post") as p:
                 p.return_value.text = "Eleven Mastercrafted"
                 response = self.client.post(url_for('Grade'),data="Narsil")
                 self.assertIn(b"Eleven Mastercrafted", response.data)



    # This test is checking that if "Goblin Cleaver"(data) and the randomly generated object Grade(g) is not equal to  
    # Eleven Mastercrafted then the function will make the outputting Grade equal to Eleven Mastercrafted which is then posted(p) to service-1.
    def test_Grade_Goblin_Cleaver(self):
        with patch("requests.get") as g:
            g.return_value.text = "Rusty"
            with patch("requests.post") as p:
                 p.return_value.text = "Eleven Mastercrafted"
                 response = self.client.post(url_for('Grade'),data="Goblin Cleaver")
                 self.assertIn(b"Eleven Mastercrafted", response.data)



    # This test is checking that if "Anduril"(data) and the randomly generated object Grade(g) is not equal to  
    # Eleven Mastercrafted then the function will make the outputting Grade equal to Eleven Mastercrafted which is then posted(p) to service-1.
    def test_Grade_Anduril(self):
        with patch("requests.get") as g:
            g.return_value.text = "Rusty"
            with patch("requests.post") as p:
                 p.return_value.text = "Eleven Mastercrafted"
                 response = self.client.post(url_for('Grade'),data="Anduril")
                 self.assertIn(b"Eleven Mastercrafted", response.data)
    


# Object modification tests for Melee_Prowess  
    


# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Melee_Prowess(g) is 1 then the result will be 5(b) because FootSoldier += 3 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Melee_Prowess(TestBase):
    def test_Melee_Prowess_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Melee_Prowess'),data="FootSoldier")
                self.assertIn(b"4", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Melee_Prowess(g) is 2 then the result will be 7(b) because Duelist += 5
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "7"
                response = self.client.post(url_for('Melee_Prowess'),data="Duelist")
                self.assertIn(b"7", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Melee_Prowess(g) is 3 then the result will be 11(b) because Berserker += 8
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "11"
                response = self.client.post(url_for('Melee_Prowess'),data="Berserker")
                self.assertIn(b"11", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Melee_Prowess(g) is 4 then the result will be 10(b) because Knight += 6
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Melee_Prowess'),data="Knight")
                self.assertIn(b"10", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 5 then the result will be 0(b) because Wizard -= 5
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "0"
                response = self.client.post(url_for('Melee_Prowess'),data="Wizard")
                self.assertIn(b"0", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 6 then the result will be 10(b) because Assassin += 4
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Melee_Prowess'),data="Assassin")
                self.assertIn(b"10", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 7 then the result will be 9 (b) because Ranger += 2
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "9"
                response = self.client.post(url_for('Melee_Prowess'),data="Ranger")
                self.assertIn(b"9", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 7 then the result will be 9 (b) because Ranger += 2
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "2"
                response = self.client.post(url_for('Melee_Prowess'),data="Druid")
                self.assertIn(b"2", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 9 then the result will be 10 (b) because Scout += 1
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Melee_Prowess'),data="Scout")
                self.assertIn(b"10", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 10 then the result will be 16 (b) because Raider += 6
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Melee_Prowess'),data="Raider")
                self.assertIn(b"16", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Melee_Prowess(g) is 10 then the result will be 17 (b) because Mercenary += 7
    # This updated object data is then posted(p) to service-1
    def test_Melee_Prowess_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "17"
                response = self.client.post(url_for('Melee_Prowess'),data="Mercenary")
                self.assertIn(b"17", response.data)



# Object modification tests for Archery_Prowess



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Archery_Prowess(g) is 1 then the result will be 5(b) because FootSoldier += 2 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Archery_Prowess(TestBase):
    def test_Archery_Prowess_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "3"
                response = self.client.post(url_for('Archery_Prowess'),data="FootSoldier")
                self.assertIn(b"3", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Archery_Prowess(g) is 2 then the result will be 7(b) because Duelist -= 3
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "-1"
                response = self.client.post(url_for('Archery_Prowess'),data="Duelist")
                self.assertIn(b"-1", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Archery_Prowess(g) is 3 then the result will be 11(b) because Berserker -= 5
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "-2"
                response = self.client.post(url_for('Archery_Prowess'),data="Berserker")
                self.assertIn(b"-2", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Archery_Prowess(g) is 4 then the result will be 10(b) because Knight += 1
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "5"
                response = self.client.post(url_for('Archery_Prowess'),data="Knight")
                self.assertIn(b"5", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 5 then the result will be 0(b) because Wizard -= 6
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "-1"
                response = self.client.post(url_for('Archery_Prowess'),data="Wizard")
                self.assertIn(b"-1", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 6 then the result will be 10(b) because Assassin += 4
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Archery_Prowess'),data="Assassin")
                self.assertIn(b"10", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 7 then the result will be 9 (b) because Ranger += 8
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Archery_Prowess'),data="Ranger")
                self.assertIn(b"15", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 8 then the result will be 2 (b) because Druid -= 4
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Archery_Prowess'),data="Druid")
                self.assertIn(b"4", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Archery_Prowessee_Prowess(g) is 9 then the result will be 10 (b) because Scout += 6
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Archery_Prowess'),data="Scout")
                self.assertIn(b"15", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 10 then the result will be 16 (b) because Raider += 4
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Archery_Prowess'),data="Raider")
                self.assertIn(b"14", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Archery_Prowess(g) is 10 then the result will be 17 (b) because Mercenary += 6
    # This updated object data is then posted(p) to service-1
    def test_Archery_Prowess_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Archery_Prowess'),data="Mercenary")
                self.assertIn(b"16", response.data)





# Object modification tests for Strength



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Strength(g) is 1 then the result will be 4(b) because FootSoldier += 3 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Strength(TestBase):
    def test_Strength_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Strength'),data="FootSoldier")
                self.assertIn(b"4", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Strength(g) is 2 then the result will be 7(b) because Duelist += 5
    # This updated object data is then posted(p) to service-1
    def test_Strength_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "7"
                response = self.client.post(url_for('Strength'),data="Duelist")
                self.assertIn(b"7", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Strength(g) is 3 then the result will be 11(b) because Berserker += 8
    # This updated object data is then posted(p) to service-1
    def test_Strength_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "11"
                response = self.client.post(url_for('Strength'),data="Berserker")
                self.assertIn(b"11", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Strength(g) is 4 then the result will be 9(b) because Knight += 5
    # This updated object data is then posted(p) to service-1
    def test_Strength_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "9"
                response = self.client.post(url_for('Strength'),data="Knight")
                self.assertIn(b"9", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Strength(g) is 5 then the result will be 1(b) because Wizard -= 4
    # This updated object data is then posted(p) to service-1
    def test_Strength_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "1"
                response = self.client.post(url_for('Strength'),data="Wizard")
                self.assertIn(b"1", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Strength(g) is 6 then the result will be 4(b) because Assassin -= 2
    # This updated object data is then posted(p) to service-1
    def test_Strength_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Strength'),data="Assassin")
                self.assertIn(b"4", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Strength(g) is 7 then the result will be 8 (b) because Ranger += 1
    # This updated object data is then posted(p) to service-1
    def test_Strength_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "8"
                response = self.client.post(url_for('Strength'),data="Ranger")
                self.assertIn(b"8", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Strength(g) is 8 then the result will be 2 (b) because Druid -= 6
    # This updated object data is then posted(p) to service-1
    def test_Strength_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "2"
                response = self.client.post(url_for('Strength'),data="Druid")
                self.assertIn(b"2", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Strength(g) is 9 then the result will be 7 (b) because Scout -= 2
    # This updated object data is then posted(p) to service-1
    def test_Strength_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "7"
                response = self.client.post(url_for('Strength'),data="Scout")
                self.assertIn(b"7", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Strength(g) is 10 then the result will be 16 (b) because Raider += 6
    # This updated object data is then posted(p) to service-1
    def test_Strength_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Strength'),data="Raider")
                self.assertIn(b"16", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Strength(g) is 10 then the result will be 17 (b) because Mercenary += 7
    # This updated object data is then posted(p) to service-1
    def test_Strength_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "17"
                response = self.client.post(url_for('Strength'),data="Mercenary")
                self.assertIn(b"17", response.data)



# Object modification tests for Endurance



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Endurance(g) is 1 then the result will be 4(b) because FootSoldier += 3 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Endurance(TestBase):
    def test_Endurance_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Endurance'),data="FootSoldier")
                self.assertIn(b"4", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Endurance(g) is 2 then the result will be 7(b) because Duelist += 5
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "7"
                response = self.client.post(url_for('Endurance'),data="Duelist")
                self.assertIn(b"7", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Endurance(g) is 3 then the result will be 13(b) because Berserker += 8
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "13"
                response = self.client.post(url_for('Endurance'),data="Berserker")
                self.assertIn(b"13", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Endurance(g) is 4 then the result will be 10(b) because Knight += 6
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Endurance'),data="Knight")
                self.assertIn(b"10", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Endurance(g) is 5 then the result will be 0(b) because Wizard -= 5
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "0"
                response = self.client.post(url_for('Endurance'),data="Wizard")
                self.assertIn(b"0", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Endurance(g) is 6 then the result will be 8(b) because Assassin += 2
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "8"
                response = self.client.post(url_for('Endurance'),data="Assassin")
                self.assertIn(b"8", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Endurance(g) is 7 then the result will be 11(b) because Ranger += 4
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "11"
                response = self.client.post(url_for('Endurance'),data="Ranger")
                self.assertIn(b"11", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Endurance(g) is 8 then the result will be 1(b) because Druid -= 7
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "1"
                response = self.client.post(url_for('Endurance'),data="Druid")
                self.assertIn(b"1", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Endurance(g) is 9 then the result will be 13(b) because Scout += 4
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "13"
                response = self.client.post(url_for('Endurance'),data="Scout")
                self.assertIn(b"13", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Endurance(g) is 10 then the result will be 16 (b) because Raider += 6
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Endurance'),data="Raider")
                self.assertIn(b"16", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Endurance(g) is 10 then the result will be 17 (b) because Mercenary += 7
    # This updated object data is then posted(p) to service-1
    def test_Endurance_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "17"
                response = self.client.post(url_for('Endurance'),data="Mercenary")
                self.assertIn(b"17", response.data)



# Object modification tests for Intelligence



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Intelligence(g) is 1 then the result will be -3(b) because FootSoldier -= 4 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Intelligence(TestBase):
    def test_Intelligence_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "-3"
                response = self.client.post(url_for('Intelligence'),data="FootSoldier")
                self.assertIn(b"-3", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Intelligence(g) is 2 then the result will be 0(b) because Duelist -= 2
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "0"
                response = self.client.post(url_for('Intelligence'),data="Duelist")
                self.assertIn(b"0", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Intelligence(g) is 3 then the result will be -3(b) because Berserker -= 6
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "-3"
                response = self.client.post(url_for('Intelligence'),data="Berserker")
                self.assertIn(b"-3", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Intelligence(g) is 4 then the result will be 2(b) because Knight -= 2
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "2"
                response = self.client.post(url_for('Intelligence'),data="Knight")
                self.assertIn(b"2", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Intelligence(g) is 5 then the result will be 13(b) because Wizard += 8
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "13"
                response = self.client.post(url_for('Intelligence'),data="Wizard")
                self.assertIn(b"13", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Intelligence(g) is 6 then the result will be 10(b) because Assassin += 4
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "10"
                response = self.client.post(url_for('Intelligence'),data="Assassin")
                self.assertIn(b"10", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Intelligence(g) is 7 then the result will be 11(b) because Ranger += 4
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "11"
                response = self.client.post(url_for('Intelligence'),data="Ranger")
                self.assertIn(b"11", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Intelligence(g) is 8 then the result will be 18(b) because Druid += 10
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "18"
                response = self.client.post(url_for('Intelligence'),data="Druid")
                self.assertIn(b"18", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Intelligence(g) is 9 then the result will be 12(b) because Scout += 3
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "12"
                response = self.client.post(url_for('Intelligence'),data="Scout")
                self.assertIn(b"12", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Intelligence(g) is 10 then the result will be 9(b) because Raider += 1
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "9"
                response = self.client.post(url_for('Intelligence'),data="Raider")
                self.assertIn(b"9", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Intelligence(g) is 10 then the result will be 15 (b) because Mercenary += 5
    # This updated object data is then posted(p) to service-1
    def test_Intelligence_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Intelligence'),data="Mercenary")
                self.assertIn(b"15", response.data)



# Object modification tests for Awareness



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Awareness(g) is 1 then the result will be 2(b) because FootSoldier += 1 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Awareness(TestBase):
    def test_Awareness_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "2"
                response = self.client.post(url_for('Awareness'),data="FootSoldier")
                self.assertIn(b"2", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Awareness(g) is 2 then the result will be 6(b) because Duelist += 4
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "6"
                response = self.client.post(url_for('Awareness'),data="Duelist")
                self.assertIn(b"6", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Awareness(g) is 3 then the result will be 4(b) because Berserker += 1
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "4"
                response = self.client.post(url_for('Awareness'),data="Berserker")
                self.assertIn(b"4", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Awareness(g) is 4 then the result will be 7(b) because Knight += 3
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "7"
                response = self.client.post(url_for('Awareness'),data="Knight")
                self.assertIn(b"7", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Awareness(g) is 5 then the result will be 15(b) because Wizard += 10
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Awareness'),data="Wizard")
                self.assertIn(b"15", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Awareness(g) is 6 then the result will be 14(b) because Assassin += 8
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Awareness'),data="Assassin")
                self.assertIn(b"14", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Awareness(g) is 7 then the result will be 13(b) because Ranger += 6
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "13"
                response = self.client.post(url_for('Awareness'),data="Ranger")
                self.assertIn(b"13", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Awareness(g) is 8 then the result will be 15(b) because Druid += 7
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Awareness'),data="Druid")
                self.assertIn(b"15", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Awareness(g) is 9 then the result will be 19(b) because Scout += 10
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "19"
                response = self.client.post(url_for('Awareness'),data="Scout")
                self.assertIn(b"19", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Awareness(g) is 10 then the result will be 13(b) because Raider += 3
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "13"
                response = self.client.post(url_for('Awareness'),data="Raider")
                self.assertIn(b"13", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Awareness(g) is 10 then the result will be 17(b) because Mercenary += 7
    # This updated object data is then posted(p) to service-1
    def test_Awareness_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "17"
                response = self.client.post(url_for('Awareness'),data="Mercenary")
                self.assertIn(b"17", response.data)



# Object modification tests for Dexterity



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Dexterity(g) is 1 then the result will be 3(b) because FootSoldier += 2 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Dexterity(TestBase):
    def test_Dexterity_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "3"
                response = self.client.post(url_for('Dexterity'),data="FootSoldier")
                self.assertIn(b"3", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Dexterity(g) is 2 then the result will be 9(b) because Duelist += 7
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "9"
                response = self.client.post(url_for('Dexterity'),data="Duelist")
                self.assertIn(b"9", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Dexterity(g) is 3 then the result will be 6(b) because Berserker += 3
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "6"
                response = self.client.post(url_for('Dexterity'),data="Berserker")
                self.assertIn(b"6", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Dexterity(g) is 4 then the result will be 8(b) because Knight += 4
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "8"
                response = self.client.post(url_for('Dexterity'),data="Knight")
                self.assertIn(b"8", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Dexterity(g) is 5 then the result will be 0(b) because Wizard -= 5
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "0"
                response = self.client.post(url_for('Dexterity'),data="Wizard")
                self.assertIn(b"0", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Dexterity(g) is 6 then the result will be 14(b) because Assassin += 8
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Dexterity'),data="Assassin")
                self.assertIn(b"14", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Dexterity(g) is 7 then the result will be 16(b) because Ranger += 9
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Dexterity'),data="Ranger")
                self.assertIn(b"16", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Dexterity(g) is 8 then the result will be 1(b) because Druid -= 7
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "1"
                response = self.client.post(url_for('Dexterity'),data="Druid")
                self.assertIn(b"1", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Dexterity(g) is 9 then the result will be 14(b) because Scout += 5
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Dexterity'),data="Scout")
                self.assertIn(b"14", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Dexterity(g) is 10 then the result will be 14(b) because Raider += 4
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Dexterity'),data="Raider")
                self.assertIn(b"14", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Dexterity(g) is 10 then the result will be 16(b) because Mercenary += 6
    # This updated object data is then posted(p) to service-1
    def test_Dexterity_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Dexterity'),data="Mercenary")
                self.assertIn(b"16", response.data)



# Object modification tests for Dodge



# This test is checking that if the profession(p) is equal to "FootSoldier"(data) and the randomly generated 
# varible Dodge(g) is 1 then the result will be 2(b) because FootSoldier += 1 
# This updated object data is then posted(p) to service-1
class Test_Service_5_Dodge(TestBase):
    def test_Dodge_FootSoldier(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"
            with patch("requests.post") as p:
                p.return_value.text = "2"
                response = self.client.post(url_for('Dodge'),data="FootSoldier")
                self.assertIn(b"2", response.data)



    # This test is checking that if the profession(p) is equal to "Duelist"(data) and the randomly generated 
    # varible Dodge(g) is 2 then the result will be 6(b) because Duelist += 4
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Duelist(self):
        with patch("requests.get") as g:
            g.return_value.text = "2"
            with patch("requests.post") as p:
                p.return_value.text = "6"
                response = self.client.post(url_for('Dodge'),data="Duelist")
                self.assertIn(b"6", response.data)



    # This test is checking that if the profession(p) is equal to "Berserker"(data) and the randomly generated 
    # varible Dodge(g) is 3 then the result will be 6(b) because Berserker -= 6
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Berserker(self):
        with patch("requests.get") as g:
            g.return_value.text = "3"
            with patch("requests.post") as p:
                p.return_value.text = "-3"
                response = self.client.post(url_for('Dodge'),data="Berserker")
                self.assertIn(b"-3", response.data)
  


    # This test is checking that if the profession(p) is equal to "Knight"(data) and the randomly generated 
    # varible Dodge(g) is 4 then the result will be 6(b) because Knight += 2
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Knight(self):
        with patch("requests.get") as g:
            g.return_value.text = "4"
            with patch("requests.post") as p:
                p.return_value.text = "6"
                response = self.client.post(url_for('Dodge'),data="Knight")
                self.assertIn(b"6", response.data)

    # This test is checking that if the profession(p) is equal to "Wizard"(data) and the randomly generated  
    # varible Dodge(g) is 5 then the result will be 0(b) because Wizard -= 5
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Wizard(self):
        with patch("requests.get") as g:
            g.return_value.text = "5"
            with patch("requests.post") as p:
                p.return_value.text = "0"
                response = self.client.post(url_for('Dodge'),data="Wizard")
                self.assertIn(b"0", response.data)



    # This test is checking that if the profession(p) is equal to "Assassin"(data) and the randomly generated  
    # varible Dodge(g) is 6 then the result will be 16(b) because Assassin += 10
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Assassin(self):
        with patch("requests.get") as g:
            g.return_value.text = "6"
            with patch("requests.post") as p:
                p.return_value.text = "16"
                response = self.client.post(url_for('Dodge'),data="Assassin")
                self.assertIn(b"16", response.data) 



    # This test is checking that if the profession(p) is equal to "Ranger"(data) and the randomly generated  
    # varible Dodge(g) is 7 then the result will be 15(b) because Ranger += 8
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Ranger(self):
        with patch("requests.get") as g:
            g.return_value.text = "7"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Dodge'),data="Ranger")
                self.assertIn(b"15", response.data) 



    # This test is checking that if the profession(p) is equal to "Druid"(data) and the randomly generated  
    # varible Dodge(g) is 8 then the result will be 1(b) because Druid -= 7
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Druid(self):
        with patch("requests.get") as g:
            g.return_value.text = "8"
            with patch("requests.post") as p:
                p.return_value.text = "1"
                response = self.client.post(url_for('Dodge'),data="Druid")
                self.assertIn(b"1", response.data)



    # This test is checking that if the profession(p) is equal to "Scout"(data) and the randomly generated  
    # varible Dodge(g) is 9 then the result will be 15(b) because Scout += 6
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Scout(self):
        with patch("requests.get") as g:
            g.return_value.text = "9"
            with patch("requests.post") as p:
                p.return_value.text = "15"
                response = self.client.post(url_for('Dodge'),data="Scout")
                self.assertIn(b"15", response.data)

    

    # This test is checking that if the profession(p) is equal to "Raider"(data) and the randomly generated  
    # varible Dodge(g) is 10 then the result will be 14(b) because Raider += 4
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Raider(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "14"
                response = self.client.post(url_for('Dodge'),data="Raider")
                self.assertIn(b"14", response.data)



    # This test is checking that if the profession(p) is equal to "Mercenary"(data) and the randomly generated  
    # varible Dodge(g) is 10 then the result will be 17(b) because Mercenary += 7
    # This updated object data is then posted(p) to service-1
    def test_Dodge_Mercenary(self):
        with patch("requests.get") as g:
            g.return_value.text = "10"
            with patch("requests.post") as p:
                p.return_value.text = "17"
                response = self.client.post(url_for('Dodge'),data="Mercenary")
                self.assertIn(b"17", response.data)