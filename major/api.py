from rest_framework import viewsets

from .serializers import MajorPlaybackSerializer
from .models import MajorPlayback


class MajorPlaybackView(viewsets.ModelViewSet):
    serializer_class = MajorPlaybackSerializer
    queryset = MajorPlayback.objects.all()

