from rest_framework.exceptions import NotFound, ValidationError
from django.db import IntegrityError
from ..model.weblinks import WebLink

class WebLinkRepository:
    @staticmethod
    def create_weblink(inputdata):
        WebLink.objects.create(**inputdata)

    @staticmethod
    def update_weblink(id, weblink):
        result = WebLink.objects.filter(id=id).update(**weblink) 

        if not result:
            raise ValidationError("웹링크 변경이 실패했습니다.")

    @staticmethod
    def delete_weblink(id):
        result = WebLink.objects.filter(id=id).delete() 

        if not result[0]:
            raise ValidationError("웹링크 삭제에 실패했습니다.")

    @staticmethod
    def get_weblink_by_id(id):
        try:
            weblink = WebLink.objects.get(pk=id)
            return weblink
        except WebLink.DoesNotExist:
            raise NotFound(f"id: {id}에 해당하는 웹링크를 찾을 수 없습니다.")

