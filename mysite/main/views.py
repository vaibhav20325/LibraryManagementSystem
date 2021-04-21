
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(response, id):
	book = Book.objects.get(id=id)
	return render(response, "main/book.html", {"book":book})

def home(response):
	return render(response, "main/home.html", {})
