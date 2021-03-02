from application import app
from flask import Flask, Response, request
import random 
import requests



# Imports the value of Weapon via post requested from service-1 and the value of Grade from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Grade", methods=["GET", "POST"])
def Grade():
    Weapon = request.data.decode('utf-8')
    
    Grade_Response = requests.get("http://service-3:5002/Grade")
    Grade_String = (Grade_Response.text)

    if Weapon == "FoeHammer":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Sting":
        Grade_String = "Eleven Mastercrafted"
    
    elif Weapon == "Narsil":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Goblin Cleaver":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Anduril":
        Grade_String = "Eleven Mastercrafted"

    Grade = Grade_String
    return Response(Grade, mimetype="text/plain")




# Imports the value of Profession via post requested from service-1 and the value of Melee_Prowess from service-3
# then reassigns the values based of the predefined rules of the below if statements
@app.route("/Melee_Prowess", methods=["GET", "POST"])
def Melee_Prowess():
    Profession = request.data.decode('utf-8')
    
    Melee_Prowess_Response = requests.get("http://service-4:5003/Melee_Prowess")
    Melee_Prowess_String = (Melee_Prowess_Response.text)
    Melee_Prowess_Int = int(Melee_Prowess_String)
    
    if Profession == "FootSoldier":
        Melee_Prowess_Int += 3
    
    elif Profession == "Duelist":
        Melee_Prowess_Int += 5
    
    elif Profession == "Berserker":
        Melee_Prowess_Int += 8
    
    elif Profession == "Knight":
        Melee_Prowess_Int += 6

    elif Profession == "Wizard":
        Melee_Prowess_Int -= 5

    elif Profession == "Assassin":
        Melee_Prowess_Int += 4

    elif Profession == "Ranger":
        Melee_Prowess_Int += 2

    elif Profession == "Druid":
        Melee_Prowess_Int -= 6
    
    elif Profession == "Scout":
        Melee_Prowess_Int += 1

    elif Profession == "Raider":
        Melee_Prowess_Int += 6

    elif Profession == "Mercenary":
        Melee_Prowess_Int += 7
         
    Melee_Prowess = str(Melee_Prowess_Int)
    return Response(Melee_Prowess, mimetype="text/plain")


# Imports the value of Profession via post requested from service-1 and the value of Archery_Prowess from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Archery_Prowess", methods=["GET", "POST"])
def Archery_Prowess():
    Profession = request.data.decode('utf-8')
    
    Archery_Prowess_Response = requests.get("http://service-4:5003/Archery_Prowess")
    Archery_Prowess_String = (Archery_Prowess_Response.text)
    Archery_Prowess_Int = int(Archery_Prowess_String)

    if Profession == "FootSoldier":
        Archery_Prowess_Int += 2
    
    elif Profession == "Duelist":
        Archery_Prowess_Int -= 3 
    
    elif Profession == "Berserker":
        Archery_Prowess_Int -= 5
    
    elif Profession == "Knight":
        Archery_Prowess_Int += 1

    elif Profession == "Wizard":
        Archery_Prowess_Int -= 6

    elif Profession == "Assassin":
        Archery_Prowess_Int += 4

    elif Profession == "Ranger":
        Archery_Prowess_Int += 8

    elif Profession == "Druid":
        Archery_Prowess_Int -= 4
    
    elif Profession == "Scout":
        Archery_Prowess_Int += 6

    elif Profession == "Raider":
        Archery_Prowess_Int += 4

    elif Profession == "Mercenary":
        Archery_Prowess_Int += 6
         
    Archery_Prowess = str(Archery_Prowess_Int)
    return Response(Archery_Prowess, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Strength from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Strength", methods=["GET", "POST"])
def Strength():
    Profession = request.data.decode('utf-8')
    
    Strength_Response = requests.get("http://service-4:5003/Strength")
    Strength_String = (Strength_Response.text)
    Strength_Int = int(Strength_String)

    if Profession == "FootSoldier":
        Strength_Int += 3
    
    elif Profession == "Duelist":
        Strength_Int += 5
    
    elif Profession == "Berserker":
        Strength_Int += 8
    
    elif Profession == "Knight":
        Strength_Int += 5

    elif Profession == "Wizard":
        Strength_Int -= 4

    elif Profession == "Assassin":
        Strength_Int -= 2

    elif Profession == "Ranger":
        Strength_Int += 1

    elif Profession == "Druid":
        Strength_Int -= 6
    
    elif Profession == "Scout":
        Strength_Int -= 2

    elif Profession == "Raider":
        Strength_Int += 6

    elif Profession == "Mercenary":
        Strength_Int += 7
         
    Strength = str(Strength_Int)
    return Response(Strength, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Endurance from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Endurance", methods=["GET", "POST"])
def Endurance():
    Profession = request.data.decode('utf-8')
    
    Endurance_Response = requests.get("http://service-4:5003/Endurance")
    Endurance_String = (Endurance_Response.text)
    Endurance_Int = int(Endurance_String)

    if Profession == "FootSoldier":
        Endurance_Int += 3
    
    elif Profession == "Duelist":
        Endurance_Int += 5
    
    elif Profession == "Berserker":
        Endurance_Int += 10
    
    elif Profession == "Knight":
        Endurance_Int += 6

    elif Profession == "Wizard":
        Endurance_Int -= 5

    elif Profession == "Assassin":
        Endurance_Int += 2

    elif Profession == "Ranger":
        Endurance_Int += 4

    elif Profession == "Druid":
        Endurance_Int -= 7
    
    elif Profession == "Scout":
        Endurance_Int += 4

    elif Profession == "Raider":
        Endurance_Int += 6

    elif Profession == "Mercenary":
        Endurance_Int += 7
         
    Endurance = str(Endurance_Int)
    return Response(Endurance, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Intelligence from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Intelligence", methods=["GET", "POST"])
def Intelligence():
    Profession = request.data.decode('utf-8')
    
    Intelligence_Response = requests.get("http://service-4:5003/Intelligence")
    Intelligence_String = (Intelligence_Response.text)
    Intelligence_Int = int(Intelligence_String)

    if Profession == "FootSoldier":
        Intelligence_Int -= 4 
    
    elif Profession == "Duelist":
        Intelligence_Int -= 2
    
    elif Profession == "Berserker":
        Intelligence_Int -= 6 
    
    elif Profession == "Knight":
        Intelligence_Int -= 2 

    elif Profession == "Wizard":
        Intelligence_Int += 8

    elif Profession == "Assassin":
        Intelligence_Int += 4

    elif Profession == "Ranger":
        Intelligence_Int += 4

    elif Profession == "Druid":
        Intelligence_Int += 10
    
    elif Profession == "Scout":
        Intelligence_Int += 3

    elif Profession == "Raider":
         Intelligence_Int -= 1
    
    elif Profession == "Mercenary":
         Intelligence_Int += 5
         
    Intelligence= str(Intelligence_Int)
    return Response(Intelligence, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Awareness from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Awareness", methods=["GET", "POST"])
def Awareness():
    Profession = request.data.decode('utf-8')
    
    Awareness_Response = requests.get("http://service-4:5003/Awareness")
    Awareness_String = (Awareness_Response.text)
    Awareness_Int = int(Awareness_String)

    if Profession == "FootSoldier":
        Awareness_Int += 1
    
    elif Profession == "Duelist":
        Awareness_Int += 4
    
    elif Profession == "Berserker":
        Awareness_Int += 1
    
    elif Profession == "Knight":
        Awareness_Int += 3

    elif Profession == "Wizard":
        Awareness_Int += 10

    elif Profession == "Assassin":
        Awareness_Int += 8

    elif Profession == "Ranger":
        Awareness_Int += 6

    elif Profession == "Druid":
        Awareness_Int += 7
    
    elif Profession == "Scout":
        Awareness_Int += 10

    elif Profession == "Raider":
         Awareness_Int += 3

    elif Profession == "Mercenary":
         Awareness_Int += 7
         
    Awareness= str(Awareness_Int)
    return Response(Awareness, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Dexterity from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Dexterity", methods=["GET", "POST"])
def Dexterity():
    Profession = request.data.decode('utf-8')
    
    Dexterity_Response = requests.get("http://service-4:5003/Dexterity")
    Dexterity_String = (Dexterity_Response.text)
    Dexterity_Int = int(Dexterity_String)

    if Profession == "FootSoldier":
        Dexterity_Int += 2
    
    elif Profession == "Duelist":
        Dexterity_Int += 7
    
    elif Profession == "Berserker":
        Dexterity_Int += 3
    
    elif Profession == "Knight":
        Dexterity_Int += 4

    elif Profession == "Wizard":
        Dexterity_Int -= 5

    elif Profession == "Assassin":
        Dexterity_Int += 8

    elif Profession == "Ranger":
        Dexterity_Int += 9

    elif Profession == "Druid":
        Dexterity_Int -= 7
    
    elif Profession == "Scout":
        Dexterity_Int += 5
    
    elif Profession == "Raider":
       Dexterity_Int += 4

    elif Profession == "Mercenary":
       Dexterity_Int += 6
         
    Dexterity = str(Dexterity_Int)
    return Response(Dexterity, mimetype="text/plain")



# Imports the value of Profession via post requested from service-1 and the value of Dodge from service-3
# then reassigns the values based of the predefined rules of the below if statements 
@app.route("/Dodge", methods=["GET", "POST"])
def Dodge():
    Profession = request.data.decode('utf-8')
    
    Dodge_Response = requests.get("http://service-4:5003/Dodge")
    Dodge_String = (Dodge_Response.text)
    Dodge_Int = int(Dodge_String)

    if Profession == "FootSoldier":
        Dodge_Int += 1
    
    elif Profession == "Duelist":
        Dodge_Int += 4
    
    elif Profession == "Berserker":
        Dodge_Int -= 6
    
    elif Profession == "Knight":
        Dodge_Int += 2

    elif Profession == "Wizard":
        Dodge_Int -= 5

    elif Profession == "Assassin":
        Dodge_Int += 10

    elif Profession == "Ranger":
        Dodge_Int += 8

    elif Profession == "Druid":
        Dodge_Int -= 7
    
    elif Profession == "Scout":
        Dodge_Int += 6

    elif Profession == "Raider":
        Dodge_Int += 4

    elif Profession == "Mercenary":
        Dodge_Int += 7
         
    Dodge = str(Dodge_Int)
    return Response(Dodge, mimetype="text/plain")