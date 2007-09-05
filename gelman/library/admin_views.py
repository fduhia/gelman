from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from gelman.library.models import Book

@staff_member_required
def book_add(request):
	if not request.POST: 
		return render_to_response( "admin/library/book/add.html");

	request.POST

