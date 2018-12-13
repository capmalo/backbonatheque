from django.db import models
from django.utils.timezone import now


class MusicianAgent(models.Model):
    name = models.TextField()


class Musician(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    birthday = models.DateField()
    nickname = models.TextField()
    band = models.TextField()
    instrument = models.TextField()
    agent = models.ForeignKey(MusicianAgent, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def age(self, today=None):
        today = today or now()
        return (today - self.birthday).days // 365


class Album(models.Model):
    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    nb_tracks = models.PositiveIntegerField()
    musician = models.ForeignKey(Musician, null=True, blank=True, on_delete=models.SET_NULL, related_name="albums")


class WriterAgent(models.Model):
    name = models.TextField()


class Writer(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    publisher = models.TextField()
    agent = models.ForeignKey(WriterAgent, null=True, blank=True, on_delete=models.SET_NULL)


class Book(models.Model):
    title = models.TextField()
    description = models.TextField()
    publication_date = models.DateField()
    writer = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="books")
