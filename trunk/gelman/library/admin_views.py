from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson
from gelman.library.models import Book

@staff_member_required
def book_add(request):
	if not request.POST: 
		return render_to_response( "admin/library/book/add.html", {'request': request});

	# Handle the POST action
	items = simplejson.loads(request.POST['items'])
	
	# Insert it into the database
	import pdb
	pdb.set_trace()


