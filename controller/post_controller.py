from flask import Blueprint, request, jsonify
import service.post_service as post_service

class PostController:
    blueprint = Blueprint('posts', __name__,url_prefix='/post')

    @staticmethod
    @blueprint.route('/', methods=['GET'])
    def get_all_posts():
        post_dto_list = post_service.PostService.get_all_posts()
        return jsonify([{
            **post_dto.__dict__,
            "user": post_dto.user.__dict__ if post_dto.user else None
        } for post_dto in post_dto_list])

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def create_post():
        post_data = request.get_json()
        post_dto = post_service.PostService.create_post(post_data)
        if not post_dto:
            return jsonify({"message": "Error creating post"}), 400
        post_representation = {
            **post_dto.__dict__,
            "user": post_dto.user.__dict__ if post_dto.user else None
        }
        return jsonify(post_representation), 201

    @staticmethod
    @blueprint.route('/<int:post_id>/', methods=['PUT'])
    def update_post(post_id):
        post_data = request.get_json()
        updated_post_dto = post_service.PostService.update_post(post_id, post_data)
        if not updated_post_dto:
            return jsonify({"message": "Post not found"}), 404
        updated_post_representation = {
            **updated_post_dto.__dict__,
            "user": updated_post_dto.user.__dict__ if updated_post_dto.user else None
        }
        return jsonify(updated_post_representation), 200

    @staticmethod
    @blueprint.route('/<int:post_id>/', methods=['DELETE'])
    def delete_post(post_id):
        deleted = post_service.PostService.delete_post(post_id)
        if not deleted:
            return jsonify({"message": "Post not found"}), 404
        return jsonify({"message": "Post successfully deleted"}), 200

