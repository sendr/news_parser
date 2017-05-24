from rest_framework import serializers
from apps.core.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('author', 'title', 'site', 'url')
