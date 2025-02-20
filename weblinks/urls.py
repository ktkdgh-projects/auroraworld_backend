from django.urls import path
from .views import create_weblink, update_weblink, delete_weblink, search_weblink

urlpatterns = [
    path('', create_weblink, name='weblink-create'),
    path('update/', update_weblink, name='weblink-update'),
    path('delete/', delete_weblink, name='weblink-delete'),
    path('search', search_weblink, name='weblink-search'),
]