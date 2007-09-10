from django.shortcuts import render_to_response, get_object_or_404
from gelman.library.models import Book

def index(request):
	recently_released = {
		'headline': "Recently Released",
		'item':  Book.objects.latest('pub_date')
	}
	return render_to_response('books/index.html',{
		'section_list': [recently_released], 
		'title': 'Gelman'})


def detail(request, isbn):
	book = get_object_or_404(Book, isbn=isbn)
	return render_to_response('books/detail.html', {'book': book})

