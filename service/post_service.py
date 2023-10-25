from domain.post import Post
from dto.post_dto import PostDTO
from repository.post_repository import PostRepository

class PostService:

    @staticmethod
    def get_all_posts():
        posts = PostRepository.get_all_posts()
        if not posts:
            return []
        return [PostDTO.from_model(post) for post in posts]

    @staticmethod
    def create_post(post_dto):
        post = Post(title=post_dto['title'], content=post_dto['content'], user_id=post_dto['user_id'])
        saved_post = PostRepository.add_post(post)
        if not saved_post:
            return None
        return PostDTO.from_model(saved_post)

    @staticmethod
    def get_post_by_id(post_id):
        post = PostRepository.get_post_by_id(post_id)
        if not post:
            return None
        return PostDTO.from_model(post)

    @staticmethod
    def update_post(post_id, updated_data):
        post = PostRepository.update_post(post_id, updated_data)
        if not post:
            return None
        return PostDTO.from_model(post)

    @staticmethod
    def delete_post(post_id):
        deleted_post = PostRepository.delete_post(post_id)
        if not deleted_post:
            return None
        return PostDTO.from_model(deleted_post)
