from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from gelman.library.models import Book, Author, Publisher
from datetime import date, datetime
from urllib import urlopen, unquote
from urlparse import urlparse
from os import path

import pdb, sys

@staff_member_required
def book_add_by_search(request):
	if not request.POST: 
		return render_to_response( "admin/library/book/add-by-search.html", {'request': request});

	# Handle the POST action
	xhr = {'succeed': [], 'failed': []};
	for item in simplejson.loads(request.POST['items']):
		publisher, created = Publisher.objects.get_or_create(name=item['publisher'])
		authors = [Author.objects.get_or_create(name=au) for au in item['authors']]
		authors = [author for (author, created) in authors];
		y,m,d = [int(x) for x in item['pub_date'].split('-')]
		pub_date = date(y, m, d)
		
		try :
			# download the image and store it to local
			dest = unquote(urlparse(item['thumburl'])[2].split('/')[-1])
			pages = int(item['pages'])
			book, created = Book.objects.get_or_create(isbn=item['isbn'], 
				title=item['title'], timestamp=datetime.now(),
				pages=pages, pub_date=pub_date, publisher=publisher,
			)
			book.authors.add(*authors)
			book.save_thumb_file(dest, urlopen(item['thumburl']).read())
			xhr['succeed'].append(item['title'])
		except :
			xhr['failed'].append(item['title'])


	# prepare the xhr
	return HttpResponse(simplejson.dumps(xhr), mimetype='text/javascript');
