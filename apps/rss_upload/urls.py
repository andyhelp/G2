from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^add',      'rss_upload.views.add'),
    (r'^list',     'rss_upload.views.list'),
    (r'^entries/(\d+)', 'rss_upload.views.entries'),
    (r'^refresh',  'rss_upload.views.refresh'),
    (r'^upload/(\d+)/(\d+)', 'rss_upload.views.upload'),
)
