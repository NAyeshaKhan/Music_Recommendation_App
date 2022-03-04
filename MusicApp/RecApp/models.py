from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username


class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="playlist", null=True)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return (
            f"{self.title} - "
            f"{self.artist}"
        )
