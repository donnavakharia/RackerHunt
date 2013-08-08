from django.conf.urls import patterns, url

urlpatterns = patterns('rackerhunt.views',
    url(r'^$', 'index'),
    url(r'^(?P<jobs_id>\d+)/$', 'detail'),
    url(r'^(?P<jobs_id>\d+)/results/$', 'results'),
    url(r'^(?P<jobs_id>\d+)/vote/$', 'vote'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
