from application import app
from flask import Flask, Response
import random 



# Defining a route that will randomly pick a characters Race via a entry from the given list
@app.route("/Race", methods=["GET"])
def Race():
    Race_List = ["Orc", "Woodland Elf", "Human", "Dwarf", "Goblin", "High Elf", "Ent", "Hobbit", "Nazgûl", "Uruk-Hai", "Dúnedain", "Orge", "Troll", "Ghost Pirate"]
    Race = Race_List[random.randrange(0,1)]
    return Response(Race,mimetype='text/plain') 



# Defining a route that will randomly pick a characters Stature via a entry from the given list
@app.route("/Stature", methods=["GET"])
def Stature():
    Stature_List = ["Tiny", "Small", "Average", "Large", "Massive", "Gigantic", "Colossal", "Stocky"]
    Stature = Stature_List[random.randrange(0,1)]
    return Response(Stature,mimetype='text/plain') 
    


# Defining a route that will randomly pick a characters Location via a entry from the given list
@app.route("/Location", methods=["GET"])
def Location():
    Location_List = ["The Shire", "Erebor", "Gondor", "Helm's Deep", "Isengard", "Lothlórien", "Mordor", "Mirkwood", "Rivendell", "Rohan", "Fangorn Forest", "Moria"]
    Location = Location_List[random.randrange(0,1)]
    return Response(Location,mimetype='text/plain') 



# Defining a route that will randomly pick a characters Rank via a entry from the given list
@app.route("/Rank", methods=["GET"])
def Rank():
    Rank_List = ["Novice", "Apprentice","Journeyman", "Adept", "Master", "Grand-Master"]
    Rank = Rank_List[random.randrange(0,1)]
    return Response(Rank,mimetype='text/plain')



# Defining a route that will randomly pick a characters Profession via a entry from the given list
@app.route("/Profession", methods=["GET"])
def Profession():
    Profession_List = ["FootSoldier","Duelist", "Berserker", "Knight", "Wizard", "Assassin", "Ranger", "Druid", "Scout", "Raider", "Mercenary"]
    Profession = Profession_List[random.randrange(0,1)]
    return Response(Profession,mimetype='text/plain')