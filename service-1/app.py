from application import app



if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
    
PicFolder = os.path.join("static","pics") #
app.config["UPLOAD_FOLDER"] = PicFolder

def multiline(fn):
    @wraps(fn)
    def _fn(*args, **kwargs):
        return "<xmp>" + fn(*args, **kwargs) + "</xmp>"
    return _fn

# Setting the Homepage for my Service
@app.route('/')
@app.route('/Home',methods=["GET"])
def Home():
    Background = os.path.join(app.config["UPLOAD_FOLDER"],"LOTR_Background.jpg")
   
   # Requesting the first set of data from service-5
    Race = requests.get("http://localhost:5001/Race")
    Stature = requests.get("http://localhost:5001/Stature")
    Location = requests.get("http://localhost:5001/Location")
    Rank = requests.get("http://localhost:5001/Rank")
    Profession = requests.get("http://localhost:5001/Profession")

    # Requesting the first set of data from service-5
    Grade = requests.get("http://localhost:5002/Grade")
    Weapon = requests.get("http://localhost:5002/Weapon")
    Stance = requests.get("http://localhost:5002/Stance")
    Trait_1 = requests.get("http://localhost:5002/Trait_1")
    Trait_2 = requests.get("http://localhost:5002/Trait_2")
    Trait_3 = requests.get("http://localhost:5002/Trait_3")


    # Requesting the first set of data from service-5 
    Melee_Prowess = requests.get("http://localhost:5004/Melee_Prowess")
    #Archery_Prowess = requests.get("http://service-5:5004/Archery_Prowess")
    #Strength = requests.get("http://service-5:5004/Strength")
    #Endurance = requests.get("http://service-5:5004/Endurance")
    #Intelligence = requests.get("http://service-5:5004/Intelligence")
    #Awareness = requests.get("http://service-5:5004/Awareness")
    #Dexterity = requests.get("http://service-5:5004/Dexterity")
    #Dodge = requests.get("http://service-5:5004/Dodge")   
    
    
    return render_template("Home.html",Background=Background,
    Race=Race.text, Stature=Stature.text, Location=Location.text,
    Rank=Rank.text, Profession=Profession.text, Grade=Grade.text, Weapon=Weapon.text, Stance=Stance.text, 
    Trait_1=Trait_1.text, Trait_2=Trait_2.text, Trait_3=Trait_3.text, Melee_Prowess=Melee_Prowess.text)

















if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0")




