from flask import Blueprint, request, jsonify
import service.user_service as service

class UserController:
    blueprint = Blueprint('users', __name__,url_prefix='/usuario')

    @staticmethod
    @blueprint.route('/', methods=['GET'])
    def get_all_users():
        userDtoLists = service.UserService.get_all_users()
        return jsonify([user_dto.__dict__ for user_dto in userDtoLists])

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def add_user():
        user_data = request.get_json()
        userDto = service.UserService.add_user(user_data)
        return jsonify(userDto.__dict__), 201
    
    @staticmethod
    @blueprint.route('/<int:user_id>/', methods=['PUT'])
    def update_user(user_id):
        user_data = request.get_json()
        updated_user = service.UserService.update_user(user_id, user_data)
        if not updated_user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(updated_user.__dict__), 200

    @staticmethod
    @blueprint.route('/<int:user_id>/', methods=['DELETE'])
    def delete_user(user_id):
        deleted_user = service.UserService.delete_user(user_id)
        if not deleted_user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(deleted_user.__dict__), 200
