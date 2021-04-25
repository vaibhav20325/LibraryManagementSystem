
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Request, Rating
from .forms import BorrowRequest, BorrowRenew
import datetime
from django.db.models import Exists, OuterRef, Count
from django.db.models.functions import Length

# Create your views here.

def home(response):
	books = Book.objects.all()

	d={}
	for book in books:
		a = len(Request.objects.filter(book = book ,status = 'Returned'))
		if a not in d:
			d[a] = []
		d[a].append(book)
	
	temp = sorted(d.keys(), reverse = True)
	popular = []
	for i in range(0,3):
		popular.extend(d[temp[i]])

	if response.method == "GET":
		if response.GET.get("search"):
			searchby = response.GET.get("searchby")
			query = response.GET.get("query")
			filter_params = {
				searchby: query
			}
			b = Book.objects.filter(**filter_params)
			books = b
	new = Book.objects.order_by('date_added')[::-1]
	new = new[0:3]
	
	'''
	popular = Book.objects.order_by(
		Count(Request.objects.filter(status = 'Returned'))
	)
	print(popular)
	'''
	return render(response, "main/home.html", {"books":books, "new": new, "popular":popular})

def index(response, id):
	
	book = Book.objects.get(id=id)
	
	try:
		r = response.user.request.filter(book = book, status = 'Issued')[0]
		temp_bool = True
	except:
		temp_bool = False

	if response.method == "POST":
		if response.POST.get("request"):
			form = BorrowRequest(response.POST)
			if form.is_valid():
				t = form.cleaned_data['time']
				req = Request(book = book, status = 'Pending', r_date = datetime.date.today(), d_date = datetime.date.today() + datetime.timedelta(t) )
				req.save()
				response.user.request.add(req)
		
		elif response.POST.get("renew"):
			form = BorrowRenew(response.POST)
			if form.is_valid():
				t = form.cleaned_data['time']
				if temp_bool:
					r = response.user.request.filter(book = book, status = 'Issued')[0]
					req = Request(book = book, status = 'Pending', r_date = datetime.date.today(), d_date = r.d_date + datetime.timedelta(t) )
					req.save()
					response.user.request.add(req)
				
				

		elif response.POST.get("rate"):
			rev = response.POST.get('review').strip()
			star = response.POST.get('rating')
			r = Rating(review = rev, rating = int(star))
			r.save()
			response.user.rating.add(r)
			book.rating.add(r)
			return render(response, "main/home.html", {})
		
		'''
		if response.POST.get("request"):
			t = response.POST.get("time")
			print(t)
			print(response.user)
		'''
	else:
		form = BorrowRequest()
	r = book.rating.all()
	list_rating = [x.rating for x in r]
	list_review = [x.review for x in r if x.review.strip() != '']
	try:
		rating = round(sum(list_rating)/len(list_rating),2)
	except:
		rating = ''

	return render(response, "main/book.html", {"book":book , "form":form, "rating":rating, "review":list_review, "user":response.user, "temp_bool":temp_bool})

def review(response):
	if response.user.is_staff:
		reqs = Request.objects.filter(status = "Pending")
		
		if response.method == "POST":
			if response.POST.get("save"):
				for req in reqs:
					r = response.POST.get("c" + str(req.id))
					if r == 'accept':
						req.status = 'Issued'
						# if quantity of each book is 1
						b = Book.objects.filter(title=req.book)
						b=b[0]
						b.availability = False
						b.status = 'Issued'
						b.save()
						req.save()
					elif r == 'reject':
						req.status = 'Rejected'
						req.save()
				reqs = Request.objects.filter(status = "Pending")
					
		return render(response, "main/review.html", {"reqs":reqs})
	else:
		return HttpResponseRedirect("/")

def profile(response):
	if response.user.is_authenticated:
		return render(response, "main/profile.html", {"user": response.user})
	else: 
		return HttpResponseRedirect("/login")

