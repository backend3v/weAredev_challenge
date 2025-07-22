from tasks.domain.repositories.user_repository import UserRepository
from tasks.domain.entities.user import User
from tasks.infrastructure.models.user_model import UserModel
from django.core.exceptions import ObjectDoesNotExist

class UserRepositoryImpl(UserRepository):
    def get_by_id(self, user_id: int) -> User | None:
        try:
            user_obj = UserModel.objects.get(id=user_id)
            return self._to_domain(user_obj)
        except ObjectDoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        try:
            user_obj = UserModel.objects.get(email=email)
            return self._to_domain(user_obj)
        except ObjectDoesNotExist:
            return None

    def create(self, user: User) -> User:
        user_obj = UserModel(
            username=user.username,
            email=user.email,
            is_active=user.is_active,
            is_staff=user.is_staff
        )
        user_obj.set_password(user.password_hash)  # password_hash stores the raw password here
        user_obj.save()
        return self._to_domain(user_obj)

    def update(self, user: User) -> User:
        user_obj = UserModel.objects.get(id=user.user_id)
        user_obj.username = user.username
        user_obj.email = user.email
        user_obj.is_active = user.is_active
        user_obj.is_staff = user.is_staff
        user_obj.save()
        return self._to_domain(user_obj)

    def delete(self, user_id: int) -> None:
        UserModel.objects.filter(id=user_id).delete()

    def authenticate(self, email: str, password: str) -> User | None:
        try:
            user_obj = UserModel.objects.get(email=email)
            if user_obj.check_password(password):
                return self._to_domain(user_obj)
            return None
        except ObjectDoesNotExist:
            return None

    def _to_domain(self, user_obj: UserModel) -> User:
        return User(
            user_id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            password_hash=user_obj.password_hash,
            is_active=user_obj.is_active,
            is_staff=user_obj.is_staff,
            created_at=user_obj.created_at,
            updated_at=user_obj.updated_at
        ) 