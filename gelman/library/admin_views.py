from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from gelman.library.models import Book, Author, Publisher
from datetime import date

import pdb, sys

@staff_member_required
def book_add_by_search(request):
	if not request.POST: 
		return render_to_response( "admin/library/book/add-by-search.html", {'request': request});

	# Handle the POST action
	xhr = {'succeed': [], 'failed': []};
	# Optimization?
	for item in simplejson.loads(request.POST['items']):
		publisher, created = Publisher.objects.get_or_create(name=item['publisher'])
		authors = [Author.objects.get_or_create(name=au) for au in item['authors']]
		authors = [author for (author, created) in authors];
		y,m,d = [int(x) for x in item['pub_date'].split('-')]
		pub_date = date(y, m, d)
		try :
			book, created = Book.objects.get_or_create(isbn=item['isbn'], name=item['title'],
				pages=300, pub_date=pub_date, publisher=publisher)
			book.authors.add(*authors)
		except :
			xhr['failed'].append(item['title'])

		xhr['succeed'].append(item['title'])

	# prepare the xhr
	return HttpResponse(simplejson.dumps(xhr), mimetype='text/javascript');

