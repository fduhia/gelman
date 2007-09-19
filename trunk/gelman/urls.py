from django.conf.urls.defaults import *

urlpatterns = patterns('',
	# static pages:
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bookstack/projects/gelman/trunk/gelman/media'}),
	(r'^repo/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/share/gelman'}),

	# login, logout
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', }),
	(r'^accounts/logout/$', 'gelman.library.views.logout_view', ),
	# admin
    (r'^admin/library/book/add-by-search', 'gelman.library.admin_views.book_add_by_search'),
    (r'^admin/', include('django.contrib.admin.urls')),

	# library
    (r'^library/', include('gelman.library.urls')),
)
