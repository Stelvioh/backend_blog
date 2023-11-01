from flask import abort, make_response, jsonify
from domain.user import User
from app import db
from sqlalchemy import exc
from werkzeug.security import check_password_hash, generate_password_hash


class UserRepository:

    @staticmethod
    def add_user(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except exc.IntegrityError:
           abort(make_response( jsonify({ "message" : "Erro ao criar usuario"}),400))

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, updated_data):
        user = User.query.get(user_id)
        if not user:
            return None
        user.name = updated_data.get('name', user.name)
        user.email = updated_data.get('email', user.email)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)

    @staticmethod
    def set_password(user, password):
        user.password = generate_password_hash(password)
        db.session.commit()