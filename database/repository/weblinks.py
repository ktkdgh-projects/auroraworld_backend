from rest_framework.exceptions import NotFound, ValidationError
from django.db import IntegrityError
from ..model.weblinks import WebLink

class WebLinkRepository:
    @staticmethod
    def create(inputdata):
        WebLink.objects.create(**inputdata)