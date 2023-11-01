# service/auth_service.py

import jwt
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import current_app
from repository.user_repository import UserRepository

class AuthService:

    @staticmethod
    def authenticate(email, password):
        user = UserRepository.get_user_by_email(email)
        if user and UserRepository.verify_password(user.password, password):  # Modifique conforme o nome do campo em seu modelo
            return AuthService.generate_token(user.user_id)
        return None

    @staticmethod
    def generate_token(user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)  # Token válido por 1 dia
        }
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm=current_app.config['JWT_ALGORITHM'])
