from rest_framework import serializers
from .models import Musician
from .models import Writer


class MusicianSerialiser(serializers.ModelSerializer):

    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"


class WriterSerialiser(serializers.ModelSerializer):

    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = "__all__"
