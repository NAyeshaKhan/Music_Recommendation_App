from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return self.title
