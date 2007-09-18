from django.conf.urls.defaults import *
from gelman.library.models import Book

cursor = {
	'queryset': Book.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^gelman/', include('gelman.foo.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bookstack/projects/gelman/trunk/gelman/media'}),
    (r'^library/$', 'gelman.library.views.index'),

    (r'^library/(?P<isbn>\d+[xX]?)/$', 'gelman.library.views.detail'),
    (r'^admin/library/book/add', 'gelman.library.admin_views.book_add'),
    (r'^admin/', include('django.contrib.admin.urls')),
)
