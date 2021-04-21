from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    summary = models.CharField(max_length = 1000)
    isbn = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    availability = models.BooleanField()

    def __str__(self):
        return self.title

