from config import db

# database model represented as python class  
class Contact(db.Model):
    # this is the key we use to indexing so primary key needs be specified 
    id = db.Column(db.Integer, primary_key=True)
    # nullable flase means it cant be empty 
    first_name=db.Column(db.String(80),unique=False,nullable=False)
    last_name=db.Column(db.String(80),unique=False,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)

    # defing  a function to take feilds from object above then convert to json to later pass it one to API  
    def to_json(self):
        return {
            "id":self.id,
            # camelcase : self.snakecase 
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email,
        }
    
    