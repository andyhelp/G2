from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^add',      'rss_upload.views.add'),
    (r'^list',     'rss_upload.views.list'),
    (r'^refresh',  'rss_upload.views.refresh'),
)
