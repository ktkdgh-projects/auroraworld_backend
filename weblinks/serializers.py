from rest_framework import serializers
from database.model.weblinks import WebLink

class WeblinkSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=255)
    name = serializers.CharField(max_length=255)
    category = serializers.ChoiceField(choices=[choice[0] for choice in WebLink._meta.get_field('category').choices])
