from rest_framework.serializers import ModelSerializer

from .models import MajorPlayback


class MajorPlaybackSerializer(ModelSerializer):
    class Meta:
        model = MajorPlayback
        fields = [
            'status',
            'album',
            'customer',
        ]
