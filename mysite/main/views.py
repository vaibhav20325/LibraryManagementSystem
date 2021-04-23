
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Request
from .forms import BorrowRequest
import datetime

# Create your views here.

def home(response):
	books = Book.objects.all()

	return render(response, "main/home.html", {"books":books})

def index(response, id):
	book = Book.objects.get(id=id)
	if response.method == "POST":
		form = BorrowRequest(response.POST)
		if form.is_valid():
			t = form.cleaned_data['time']
			req = Request(book = book, status = 'Pending', r_date = datetime.date.today(), d_date = datetime.date.today() + datetime.timedelta(t) )
			req.save()
			response.user.request.add(req)
		'''
		if response.POST.get("request"):
			t = response.POST.get("time")
			print(t)
			print(response.user)
		'''
	else:
		form = BorrowRequest()
	return render(response, "main/book.html", {"book":book , "form":form})

def review(response):
	if response.user.is_staff:
		reqs = Request.objects.filter(status = "Pending")
		return render(response, "main/review.html", {"reqs":reqs})
	else:
		return HttpResponseRedirect("/")

def profile(response):
	if response.user.is_authenticated:
		return render(response, "main/profile.html", {"user": response.user})
	else: 
		return HttpResponseRedirect("/login")

