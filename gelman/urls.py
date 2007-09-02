from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^gelman/', include('gelman.foo.urls')),

    (r'^library/(?P<isbn>\d+)/$', 'gelman.library.views.detail'),
    (r'^admin/', include('django.contrib.admin.urls')),
)
