from rest_framework import serializers

from .models import Text

class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ('name', 'alias')