from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SGGapp.views.home', name='home'),
    # url(r'^SGGapp/', include('SGGapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^location$', 'location.views.BinLocs'),
    url(r'^binloc$', 'sggserver.location.views.bin_locs'),
    url(r'^srequest$', 'sggserver.srequest.views.get_post'),
    url(r'^matrix$', 'sggserver.matrix.views.get_matrix'),
    url(r'^zerow$', 'sggserver.zerow.views.get_text'),
    url(r'^metrics$', 'sggserver.metrics.views.get_metrics'),
)
