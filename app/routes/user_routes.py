from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from app.crypt import bcrypt
from app.db import db
from app.models.user import User
from app.utils import response_error, response_success

user_route = Blueprint("user_route", __name__)


# READ ALL
@user_route.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        users_data = [user.to_json() for user in users]
        return response_success(users_data)
    except Exception as e:
        return response_error(str(e), 500)


# READ
@user_route.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            user_data = {
                "name": user.name,
                "email": user.email,
            }
            return response_success(user_data)
        else:
            return response_error("User not found", 404)
    except Exception as e:
        return response_error(str(e), 500)


# REGISTER
@user_route.route("/register", methods=["POST"])
def register():
    print(request)
    try:
        # Get data from form or JSON
        name = request.json.get("name")
        email = request.json.get("email")
        plain_text_password = request.json.get("password")

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(plain_text_password).decode(
            "utf-8"
        )

        # Create new user and save to database
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return response_success("User registered successfully", 201)

    except IntegrityError:
        return response_error("That username or email already exists")
    except Exception as e:
        return response_error(str(e))


# LOGIN
@user_route.route("/login", methods=["POST"])
def login():
    try:
        email = request.json.get("email")
        password = request.json.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response_error("Incorrect username or email")
        if not bcrypt.check_password_hash(user.password, password):
            return response_error("Incorrect username or email")

        return response_success({"user": user.to_json()})
    except Exception as e:
        return response_error(str(e))
