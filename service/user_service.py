import jwt
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import current_app
from domain.user import User
from dto.user_dto import UserDTO
from repository.user_repository import UserRepository

class UserService:

    @staticmethod
    def get_all_users():
         users =  UserRepository.get_all_users()
         if not users:
             return []
         return [UserDTO.from_model(user) for user in users]
        
    
    @staticmethod
    def add_user(user_dto):
        user = User(name=user_dto['name'], email=user_dto['email'], password=user_dto['password'])
        if not user:
            return
        return UserDTO.from_model(UserRepository.add_user(user))

    @staticmethod
    def update_user(user_id, updated_data):
        user = UserRepository.update_user(user_id, updated_data)
        if not user:
            return None
        return UserDTO.from_model(user)

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.delete_user(user_id)
        if not user:
            return None
        return UserDTO.from_model(user)
    
    @staticmethod
    def authenticate(email, password):
        user = UserRepository.get_user_by_email(email)
        if user and UserRepository.verify_password(user.password, password): 
            return user, UserService.generate_token(user.user_id) # return user e token
        return None, None

    @staticmethod
    def generate_token(user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)  # Token válido por 1 dia
        }
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm=current_app.config['JWT_ALGORITHM'])
