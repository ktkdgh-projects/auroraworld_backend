from django.http import Http404
from ..model.users import User

class UserRepository:
    @staticmethod
    def get_user_by_id(id):
        print(id)
        try:
            user = User.objects.get(pk=id)
            return user
        except User.DoesNotExist:
            raise Http404(f"User with id: {id} not found.")
