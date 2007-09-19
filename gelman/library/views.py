from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from gelman.library.models import Book

def index(request):
	recently_released = {
		'headline': "Recently Released",
		'items':  Book.objects.all().order_by('-pub_date')[:5]
	}
	
	recently_added = {
		'headline': "Recently Added",
		'items':  Book.objects.all().order_by('-timestamp')[:5]
	}
	return render_to_response('library/index.html',{
		'section_list': [recently_released, recently_added], 
		'user': request.user})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/library')


def book_detail(request, isbn):
	book = get_object_or_404(Book, isbn=isbn)
	return render_to_response('library/book_detail.html', {'item': book})

