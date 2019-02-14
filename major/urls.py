from rest_framework.routers import DefaultRouter

from .api import MajorPlaybackView

major_router = DefaultRouter()
major_router.register(r"major/playback", MajorPlaybackView, basename="major-playback")
