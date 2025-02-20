from rest_framework.exceptions import NotFound
from django.db.models import Q
from ..model.shares import Share

class ShareRepository:
    @staticmethod
    def get_share_by_user_with_weblink(user, weblink):
        try:
            share = Share.objects.get(shared_with_user=user, shared_by_weblink=weblink)
            return share
        except Share.DoesNotExist:
            raise NotFound(f"해당하는 웹링크 공유를 찾을 수 없습니다.")

    @staticmethod
    def get_share_by_shared_with_user(shared_with_user, keyword, category):
        filter_conditions = Q(shared_with_user=shared_with_user)
        
        if keyword:
            filter_conditions &= Q(shared_by_weblink__name__icontains=keyword)

        if category:
            filter_conditions &= Q(shared_by_weblink__category=category)

        shares = Share.objects.filter(filter_conditions)
        return shares
