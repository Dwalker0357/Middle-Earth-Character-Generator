from flask import request, Response
import requests
from application import app
import random



# Defining a route that will randomly pick a characters Grade via a entry from the given list
@app.route("/Grade", methods=["GET"])
def Grade():
    Grade_List = ["Broken", "Rusty", "Shoddy", "Blunt", "Serviceable", "Honed", "Freshy Forged" ,"Eleven Mastercrafted" ,"Dwarven Mastercrafted"]
    Grade = Grade_List[random.randrange(0,9)]
    return Response(Grade,mimetype='text/plain')


# Defining a route that will randomly pick a characters Weapon via a entry from the given list
@app.route("/Weapon", methods=["GET"])
def Weapon():
    Weapon_List = ["Barefist", "Dagger", "ShortSword", "LongSword", "Morning star", "Two-Handed GreatSword" , "Two-Handed BattleAxe","Dual-Wield Daggers", 
    "Dual-Wield Short Axes", "Dual-Wield Short Swords", "Dual-Wield Long Swords", "ShortBow", "Longbow", "Crossbow", "Cavalry Bow", "ShortSword And Shield", 
    "LongSword And Shield", "Morning Star And Shield" "Polearm", "Warhammer","Spiked Fist", "Short Axe And Shield", "Elfen Sabre", "Falchion", "FoeHammer", 
    "Sting", "Morgul Blade", "Narsil", "Goblin Cleaver", "Anduril"]
    Weapon = Weapon_List[random.randrange(0,29)]
    return Response(Weapon,mimetype='text/plain')


# Defining a route that will randomly pick a characters Stance via a entry from the given list
@app.route("/Stance", methods=["GET"])
def Stance():
    Stance_List = ["Clumsy", "Light-Footed", "Lightning Fast", "Rock Solid", "Immovable", "Veteran Combatant", "Martial Artist", "Cripple"]
    Stance = Stance_List[random.randrange(0,8)]
    return Response(Stance,mimetype='text/plain')


# Defining a route that will randomly pick a characters Trait_1 via a entry from the given list
@app.route("/Trait_1", methods=["GET"])
def Trait_1():
    Trait_1_List = ["Odin Force Disease Resist", "Sickly", "Built Different", "Pigeon Chest", "Massive Natural Biceps", "Kleptomaniac",
    "Savant","Cracked Personality", "Slight of Hand", "Pyromaniac", "Arsenist", "Mystic", "Mental", "High"]
    Trait_1 = Trait_1_List[random.randrange(0,14)]
    return Response(Trait_1,mimetype='text/plain')


# Defining a route that will randomly pick a characters Trait_2 via a entry from the given list
@app.route("/Trait_2", methods=["GET"])
def Trait_2():
    Trait_2_List = ["Orc Hater", "Human Hater", "Elf Hater", "Dwarf Hater", "Goblin Hater", "Hobbit Hater", "Idiot", "Genius", "Fearless", 
    "Odin Force Healing", "Expert Horse Rider", "God Fearing", "Blind", "Evil", "Naive", "Grizzled"]
    Trait_2 = Trait_2_List[random.randrange(0,16)]
    return Response(Trait_2,mimetype='text/plain')


# Defining a route that will randomly pick a characters Trait_3 via a entry from the given list
@app.route("/Trait_3", methods=["GET"])
def Trait_3():
    Trait_3_List = ["Natural Sprinter", "Low Stamina", "Unending Stamina", "Grand-Master Strategist", "Weak", "Stonks", "Paranoid", "Heroic", "Anemic",
    "Grumpy","Lazy", "Confused", "Drunk", "Troubled", "Damaged", "Snapped Up", "Hench"]
    Trait_3 = Trait_3_List[random.randrange(0,17)]
    return Response(Trait_3,mimetype='text/plain')