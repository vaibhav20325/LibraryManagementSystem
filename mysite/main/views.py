
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BorrowRequest

# Create your views here.

def index(response, id):
	book = Book.objects.get(id=id)
	form = BorrowRequest()
	return render(response, "main/book.html", {"book":book , "form":form})

def home(response):
	return render(response, "main/home.html", {})
