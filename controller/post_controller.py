from flask import Blueprint, request, jsonify
import service.post_service as post_service

class PostController:
    blueprint = Blueprint('posts', __name__,url_prefix='/post')

    @staticmethod
    @blueprint.route('/', methods=['GET'])
    def get_all_posts():
        post_dto_list = post_service.PostService.get_all_posts()
        return jsonify([post_dto.__dict__ for post_dto in post_dto_list])

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def create_post():
        post_data = request.get_json()
        post_dto = post_service.PostService.create_post(post_data)
        return jsonify(post_dto.__dict__), 201

    @staticmethod
    @blueprint.route('/<int:post_id>/', methods=['PUT'])
    def update_post(post_id):
        post_data = request.get_json()
        updated_post = post_service.PostService.update_post(post_id, post_data)
        if not updated_post:
            return jsonify({"message": "Post not found"}), 404
        return jsonify(updated_post.__dict__), 200

    @staticmethod
    @blueprint.route('/<int:post_id>/', methods=['DELETE'])
    def delete_post(post_id):
        deleted_post = post_service.PostService.delete_post(post_id)
        if not deleted_post:
            return jsonify({"message": "Post not found"}), 404
        return jsonify(deleted_post.__dict__), 200
