from rest_framework import serializers

from .models import UrlObject   


class UrlObjectSerializer(serializers.ModelSerializer):
    shorten_url = serializers.SerializerMethodField()

    class Meta:
        model = UrlObject
        fields = ['original_url', 'shorten_url']

    def get_shorten_url(self, obj):
        return obj.get_url()

