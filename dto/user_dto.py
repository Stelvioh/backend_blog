class UserDTO:
    def __init__(self, user_id, name, email, password=None):  
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def from_model(model):
        return UserDTO(user_id=model.user_id, name=model.name, email=model.email, password=model.password) 