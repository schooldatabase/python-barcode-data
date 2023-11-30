from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio_url = models.URLField()
    video_url = models.URLField(null=True, blank=True)

class Podcast(models.Model):
    title = models.CharField(max_length=100)
    audio_url = models.URLField()
    video_url = models.URLField(null=True, blank=True)

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists')

class Album(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='albums')

class Blend(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class PremiumPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    months = models.PositiveIntegerField(choices=[(1, '1 Month'), (2, '2 Months'), (3, '3 Months')])

# Add more fields and functionalities as needed
