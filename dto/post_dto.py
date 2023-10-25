from dto.user_dto import UserDTO


class PostDTO:
    def __init__(self, post_id, title, content, user_id, created_at, user=None):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = created_at
        self.user = user  # Armazenará o UserDTO associado

    @staticmethod
    def from_model(model):
        user_dto = None
        if model.user:
            user_dto = UserDTO.from_model(model.user)
        return PostDTO(
            post_id=model.post_id,
            title=model.title,
            content=model.content,
            user_id=model.user_id,
            created_at=model.created_at,
            user=user_dto
        )
