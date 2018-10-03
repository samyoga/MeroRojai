from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=250)
    book_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    book_cover = models.CharField(max_length=1000)

class Movie(models.Model):
    casts = models.CharField(max_length=500)
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    movie_poster = models.CharField(max_length=1000)


