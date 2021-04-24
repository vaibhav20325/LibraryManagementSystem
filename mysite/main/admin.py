from django.contrib import admin
from .models import Book, Request, Rating
# Register your models here.
admin.site.register(Book)
admin.site.register(Request)
admin.site.register(Rating)
