from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from gelman.library.models import Book, Author, Publisher, File, FileType
from datetime import date, datetime
from urllib import urlopen, unquote, urlretrieve
from urlparse import urlparse
from os import path

import pdb, sys

@staff_member_required
def book_add_by_search(request):
	if not request.POST: 
		return render_to_response( "admin/library/book/add-by-search.html", {'request': request});

	# Handle the meta
	item = simplejson.loads(request.POST['meta'])
	publisher, created = Publisher.objects.get_or_create(name=item['publisher'])
	authors = [Author.objects.get_or_create(name=au) for au in item['authors']]
	authors = [author for (author, created) in authors];
	y,m,d = [int(x) for x in item['pub_date'].split('-')]
	pub_date = date(y, m, d)
	try :
		# download the image and store it to local
		pages = int(item['pages'])
		book, created = Book.objects.get_or_create(isbn=item['isbn'], 
			title=item['title'], timestamp=datetime.now(),
			pages=pages, pub_date=pub_date, publisher=publisher,
		)
		pdb.set_trace()
		if created:
			thumb = unquote(urlparse(item['thumburl'])[2].split('/')[-1])
			cover = unquote(urlparse(item['coverurl'])[2].split('/')[-1])
			# using hard-coded image temporary
			urlretrieve(item['thumburl'], path.join(settings.MEDIA_ROOT, 'images', thumb))
			urlretrieve(item['coverurl'], path.join(settings.MEDIA_ROOT, 'images', cover))

			book.thumb = path.join('images', thumb);
			book.cover = path.join('images', cover);
			book.authors.add(*authors)
			book.save()

		# TODO : Add check whether the file is already saved, using md5sum?
		handle = request.FILES['handle']
		if handle:
			ft, created = FileType.objects.get_or_create(type=FileType.parse(handle['filename']))
			filename = book.isbn + '-' + book.title
			file, created = File.objects.get_or_create(type=ft, meta=book)
			file.save_handle_file(filename, handle['content'])
			file.save()
	except :
		return HttpResponse("<textarea>failed.</textarea>", mimetype='text/html');
		#return HttpResponse(simplejson.dumps(xhr), mimetype='text/javascript');
	return HttpResponse("<textarea>got it</textarea>", mimetype='text/html');
