from domain.user import User
from dto.user_dto import UserDTO
from repository.user_repository import UserRepository

class UserService:

    @staticmethod
    def get_all_users():
         users =  UserRepository.get_all_users()
         if not users:
             return []
         return [UserDTO.from_model(user) for user in users]
        
    
    @staticmethod
    def add_user(user_dto):
        user = User(name=user_dto['name'], email=user_dto['email'])
        if not user:
            return
        return UserDTO.from_model(UserRepository.add_user(user))

    @staticmethod
    def update_user(user_id, updated_data):
        user = UserRepository.update_user(user_id, updated_data)
        if not user:
            return None
        return UserDTO.from_model(user)

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.delete_user(user_id)
        if not user:
            return None
        return UserDTO.from_model(user)