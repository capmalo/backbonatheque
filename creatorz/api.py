from rest_framework import viewsets
from .serializers import MusicianSerialiser
from .serializers import WriterSerialiser

from .models import Musician
from .models import Writer


class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MusicianSerialiser
    queryset = Musician.objects.all()


class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WriterSerialiser
    queryset = Writer.objects.all()
