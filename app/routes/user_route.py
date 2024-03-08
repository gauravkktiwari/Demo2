from flask import request, jsonify, Blueprint
from app.dao import user_dao as userDao

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods = ["GET"])
def get_users():

    users = userDao.getUsers()

    if len(users) > 0:
        return jsonify({
            "status":1,
            "message":"success",
            "list": [user.serialize() for user in users]
        })
    else:
        return jsonify({
            "status":0,
            "message":"Data not found!"
        })
    
@user_bp.route("/createUser", methods = ["POST"])
def create_user():
    try:
        data = request.get_json()

        if data is None or not(bool(data)):
            return jsonify({
                "status":0,
                "message":"Please enter data"
            })
        elif "userName" not in request.json:
            return jsonify({
                "status":0,
                "message":"Please enter userName"
            })
        elif "userEmail" not in request.json:
            return jsonify({
                "status":0,
                "message":"Please enter userEmail"
            })
        user = userDao.createUser(data["userName"], data["userEmail"])

        if user is not None:
            return jsonify({
                "status":1,
                "message":"Success",
                "userId":user.user_id
            })
        else:
            return jsonify({
                "status":0,
                "message":"Data not saved"
            })
    
    except Exception as e:
        print("Error: ",e)
    
    return jsonify({"status":0,"message":"Failure"}), 201