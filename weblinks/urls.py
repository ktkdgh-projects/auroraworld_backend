from django.urls import path
from .views import create_weblink

urlpatterns = [
    path('', create_weblink, name='weblink'),
]