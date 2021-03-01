from application import db

# Setting up our db.model that corresponds to an MYSQL database tabel 

class lotr_character(db.Model):
	# ID and character name
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    
    # First set of Objects from objects from service-2
    race = db.Column(db.String(25), nullable=False)
    stature = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(25), nullable=False)
    rank = db.Column(db.String(25), nullable=False)
    profession = db.Column(db.String(25), nullable=False)
    
    # second set of objects from service-3
    grade = db.Column(db.String(25), nullable=False)
    weapon = db.Column(db.String(25), nullable=False)
    stance = db.Column(db.String(25), nullable=False)
    trait_1 = db.Column(db.String(25), nullable=False)
    trait_2 = db.Column(db.String(25), nullable=False)
    trait_3 = db.Column(db.String(25), nullable=False)

    # Thrid set of objects from service-5 
    melee_prowess = db.Column(db.String(22), nullable=False)
    archery_prowess = db.Column(db.String(2), nullable=False)
    strength = db.Column(db.String(2), nullable=False)
    endurance = db.Column(db.String(2), nullable=False)
    intelligence = db.Column(db.String(2), nullable=False)
    awareness = db.Column(db.String(2), nullable=False)
    dexterity = db.Column(db.String(2), nullable=False)
    dodge = db.Column(db.String(2), nullable=False)

    