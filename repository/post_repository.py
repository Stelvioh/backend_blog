from database import db
from domain.post import Post
from flask import abort, make_response, jsonify
from sqlalchemy.orm import joinedload
from sqlalchemy import exc

class PostRepository:

    @staticmethod
    def add_post(post):
        try:
            db.session.add(post)
            db.session.commit()
            return post
        except exc.IntegrityError:
            abort(make_response(jsonify({"message": "Error while creating post"}), 400))

    @staticmethod
    def get_all_posts():
        return Post.query.options(joinedload(Post.user)).all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.options(joinedload(Post.user)).get(post_id)

    @staticmethod
    def update_post(post_id, updated_data):
        post = Post.query.options(joinedload(Post.user)).get(post_id)
        if not post:
            return None
        post.title = updated_data.get('title', post.title)
        post.content = updated_data.get('content', post.content)
        db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.options(joinedload(Post.user)).get(post_id)
        if not post:
            return None
        db.session.delete(post)
        db.session.commit()
        return post

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).options(joinedload(Post.user)).all()
