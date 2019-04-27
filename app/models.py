from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80),unique = True)
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    profile_photo = db.Column(db.String(80))
    joined_on = db.Column(db.Date) 
    
    
    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo, joined_on):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname 
        self.lastname = lastname
        self.email = email 
        self.location = location
        self.biography = biography 
        self.profile_photo = profile_photo 
        self.joined_on = joined_on 
    
    
class UserPost(db.Model):
    __tablename__ = 'user_post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    photo = db.Column(db.String(80))
    caption = db.Column(db.String(80))
    created_on = db.Column(db.Date)
    
    def __init__(self, user_id, photo, caption, created_on):
        self.user_id = user_id 
        self.photo = photo
        self.caption = caption 
        self.created_on = created_on 
    
class UserLikes(db.Model):
    __tablename__ = 'user_likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)
    
    
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id 
    
class UserFollows(db.Model):
    __tablename__ = 'user_follows'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)  
    
    
    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id 
 