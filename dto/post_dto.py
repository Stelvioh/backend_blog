class PostDTO:
    def __init__(self, post_id, title, content, user_id, created_at):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = created_at

    @staticmethod
    def from_model(model):
        return PostDTO(
            post_id=model.post_id,
            title=model.title,
            content=model.content,
            user_id=model.user_id,
            created_at=model.created_at
        )
