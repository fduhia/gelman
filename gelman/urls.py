from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^gelman/', include('gelman.foo.urls')),

    (r'^library/(?P<isbn>\d+[xX]?)/$', 'gelman.library.views.detail'),
    (r'^library/$', 'gelman.library.views.index'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bookstack/projects/media'}),
    (r'^admin/library/book/add', 'gelman.library.admin_views.book_add'),
    (r'^admin/', include('django.contrib.admin.urls')),
)
