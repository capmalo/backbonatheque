from django.db import models


class MajorPlayback(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    STATUS_PLAYSTART = "START"
    STATUS_PLAYSTOP = "STOP"
    STATUS_CHOICES = (
        (STATUS_PLAYSTART, "Playback started"),
        (STATUS_PLAYSTOP, "Playback ended"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    album = models.PositiveIntegerField("Album ID")
    customer = models.PositiveIntegerField("User ID")
