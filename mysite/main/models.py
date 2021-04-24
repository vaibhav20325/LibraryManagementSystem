from django.db import models
from django.contrib.auth.models import User

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
    status = models.CharField(max_length = 10, default = 'returned')
    def __str__(self):
        return self.title

class Request(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'request', null = True)
    status = models.CharField(max_length = 20)
    #Returned / Issued / Pending / Rejected
    r_date = models.DateField(null = True)
    d_date = models.DateField(null = True)
    book = models.CharField(max_length = 200)
    #id = models.IntegerField(primary_key = True)
    def __str__(self):
        return str(self.id)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'rating', null = True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE,related_name = 'rating', null = True)
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)

