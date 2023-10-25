from flask import abort, make_response, jsonify
from domain.user import User
from app import db
from sqlalchemy import exc

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