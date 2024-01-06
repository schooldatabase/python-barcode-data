"""from django.db import models
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










######################################################################



you can generate spotify clone in drf generic view ,  DjangoFilterBackend, SearchFilter
you can used requirement any python library 

include functionality 

listing : songs/music, podcasts : audio (.mp3 format), video (.mp4 format) and watching choices (low, normal, high)
functionality podcasts : audio (.mp3 format), video (.mp4 format) add & shows or create & list 
functionality song : 
song fields : title, descrition,artist, audio(.mp3),vidio(.mp4)
song method : count song, like song


storing data : artists, playlists, album
artists : authentication user list / retrieve only
artists show credits : performed by ,  written by ,  produced by

artists following


playlist : create/ build a playlist with songs or episodes 
functionality playlist : add songs, remove songs, list, retrieve from playlist ( user)
playlist polices : choices (private, public)
playlist enhanced 

album : create/ build a album with songs 
album functionality : add songs, remove songs, update, list , destroy  from album (only admin )

album like : 
like, downloads (with permieum)
like all songs (user/admin)

blend : combine tastes in a shared playlist with firends invite friends to blend 

queue : add to  queue

listen to music ad-free (premieum) : add list premium plan (month wise choices 1,2,3)
download : song, playlist 
download functionality: choices (low, normal, high)
add list premium plan (month wise choices 1,2,3)



wtite all code 























"""