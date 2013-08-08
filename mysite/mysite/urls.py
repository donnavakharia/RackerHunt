from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^rackerhunt/$', 'rackerhunt.views.index'),
    url(r'^jobs/(?P<jobs_id>\d+)/$', 'rackerhunt.views.detail'),
    url(r'^jobs/(?P<jobs_id>\d+)/results/$', 'rackerhunt.views.results'),
    url(r'^jobs/(?P<jobs_id>\d+)/vote/$', 'rackerhunt.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
