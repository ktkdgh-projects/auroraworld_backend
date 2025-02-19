from rest_framework.exceptions import NotFound, ValidationError
from django.db import IntegrityError
from ..model.shares import Share

class ShareRepository:
    @staticmethod
    def get_share_by_user_with_weblink(user, weblink):
        try:
            share = Share.objects.get(shared_with_user=user, shared_by_weblink=weblink)
            return share
        except Share.DoesNotExist:
            raise NotFound(f"해당하는 웹링크 공유를 찾을 수 없습니다.")
