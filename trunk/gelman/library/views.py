from django.shortcuts import render_to_response, get_object_or_404
from gelman.library.models import Book

def detail(request, isbn):
	book = get_object_or_404(Book, isbn13=isbn)
	return render_to_response('books/detail.html', {'book': book})

