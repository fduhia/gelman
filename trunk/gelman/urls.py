from django.conf.urls.defaults import *
from gelman.library.models import Book

cursor = {
	'queryset': Book.objects.all(),
}

urlpatterns = patterns('',
	# static pages:
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bookstack/projects/gelman/trunk/gelman/media'}),
	# index, login, logout
    (r'^library/$', 'gelman.library.views.index'),
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', }),
	(r'^accounts/logout/$', 'gelman.library.views.logout_view', ),

    (r'^library/(?P<isbn>\d+[xX]?)/$', 'gelman.library.views.detail'),
    (r'^admin/library/book/add', 'gelman.library.admin_views.book_add'),
    (r'^admin/', include('django.contrib.admin.urls')),
)
