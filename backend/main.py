# creating CRUD APP (create read update and delete)
from flask import request, jsonify
from config import app, db
from models import Contact

@app.route('/contacts',methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    # creating the list of json contacts using lambda function and map one attribute after other 
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

if __name__ == "__main__":
    # getting the context of application
    with app.app_context():
        db.create_all()
        # create all the models defined in the database , spin_up the DB if not yet created


# running on localhost and endpoint is gonna be create_contact
# i.e localhost:5000/create_conatct



# -to create what do we need
# -first_name
# -last_name
# -email

# request type :
# datatype: JSON

# type : GET , POST , PATCH , DELETE 

# backend gives response with status : 200(success) or 404(error)


