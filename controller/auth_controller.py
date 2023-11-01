# controller/auth_controller.py

from flask import Blueprint, request, jsonify
import service.auth_service as AuthService

class AuthController:
    blueprint = Blueprint('auth', __name__, url_prefix='/auth')

    @staticmethod
    @blueprint.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        token = AuthService.authenticate(email, password)
        
        if token:
            return jsonify({"message": "Login successful", "token": token.decode('utf-8')}), 200
        return jsonify({"message": "Invalid email or password"}), 401
