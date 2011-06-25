# -*- coding: utf-8 -*-
import os.path

from django.conf.urls.defaults import *
import pydj.playlist.views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

defaultdict = { 'groupName': 'example' }

urlpatterns = patterns('',
    # Example:
    # (r'^pydj/', include('pydj.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

#(r'^community/', include('sphene.community.urls'), defaultdict),
#(r'^board/', include('sphene.sphboard.urls'), defaultdict),

# Only for development
#(r'^.*sphene/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/static/sphene' }),
(r'^forum/', include('forum.urls')),
(r'^admin/', include(admin.site.urls)),
(r'^$', 'pydj.playlist.views.playlist'),
(r'^playlist(/(?P<lastid>\d+))?$', 'pydj.playlist.views.playlist', {}, "playlist"),
(r'^splaylist$', 'pydj.playlist.views.splaylist'),
(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMAGES_DIR}),
(r'^emoticons/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.IMAGES_DIR, "emoticons")}, "emoticons"),
(r'^upload/?$', 'pydj.playlist.views.upload'),
(r'^stats/?$', 'pydj.playlist.views.globalstats'),     
(r'^search/?$', 'pydj.playlist.views.search'),
(r'^comment/(\d+)$', 'pydj.playlist.views.comment'),
(r'^comment/(?P<commentid>\d+)/delete$', 'pydj.playlist.views.delete_comment', {}, "delete_comment"),
(r'^artist/(?P<artistid>\d+)$', 'pydj.playlist.views.artist', {}, "artist"),
(r'^user/(?P<userid>\d+)$', 'pydj.playlist.views.user', {}, "user"),
(r'^user/(?P<userid>\d+)/givetoken$', 'pydj.playlist.views.give_token', {}, "give_token"),
(r'^.*/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMAGES_DIR}),
(r'^.*/emoticons/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.IMAGES_DIR, "emoticons")}, "emoticons"),
(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
{'document_root': "/usr/lib/python2.5/site-packages/django/contrib/admin/media/"}),
(r'^.*login/?$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, 'login'),
(r'^logout/?$', 'django.contrib.auth.views.logout_then_login'),
(r'^add/(?P<songid>\d+)$', 'pydj.playlist.views.add'), 
(r'^next/(?P<authid>.+)$', 'pydj.playlist.views.next'), 
(r'^register/?$', 'pydj.playlist.views.newregister'), 
(r'^song/(?P<songid>\d+)(?P<edit>/edit)?$', 'pydj.playlist.views.song', {}, "song"),
(r'^song/(?P<songid>\d+)/rate/(?P<vote>\d+)/$', 'pydj.playlist.views.rate'),
(r'^song/(?P<songid>\d+)/ban$', 'pydj.playlist.views.bansong'),
(r'^song/(?P<songid>\d+)/download$', 'pydj.playlist.views.download_song'),
(r'^song/(?P<songid>\d+)/delete$', 'pydj.playlist.views.deletesong'),
(r'^song/(?P<songid>\d+)/delete/(?P<confirm>.+)$', 'pydj.playlist.views.deletesong'),
(r'^song/(?P<songid>\d+)/report$', 'pydj.playlist.views.song_report'),
(r'^song/(\d+)/unban/?(\d+)$', 'pydj.playlist.views.unbansong'),
(r'^song/(\d+)/merge/(\d+)$', 'pydj.playlist.views.merge_song'),
(r'^playlist/remove/(\d+)$', 'pydj.playlist.views.removeentry'), 
(r'^reports$', 'pydj.playlist.views.reports', {}, "reports"), 
(r'^reports/approve/(?P<approve>\d+)', 'pydj.playlist.views.reports'), 
(r'^reports/deny/(?P<deny>\d+)', 'pydj.playlist.views.reports'), 
(r'^editqueue/?$', 'pydj.playlist.views.edit_queue', {}, "edit_queue"), 
(r'^editqueue/approve/(?P<approve>\d+)', 'pydj.playlist.views.edit_queue'), 
(r'^editqueue/deny/(?P<deny>\d+)', 'pydj.playlist.views.edit_queue'), 
(r'^album/(\d+)$', 'pydj.playlist.views.album', {}, "album"), 
(r'^skip$', 'pydj.playlist.views.skip'), 
(r'^artists/(123|all|\w)/(\d+)$', 'pydj.playlist.views.listartists'), 
(r'^api/(?P<resource>.+)$', 'pydj.playlist.views.api'), 
(r'^ajax$', 'pydj.playlist.views.ajax'), 
(r'^favourite/(?P<songid>\d+)$', 'pydj.playlist.views.favourite'), 
(r'^unfavourite/(?P<songid>\d+)$', 'pydj.playlist.views.unfavourite'), 
(r'^settings/?$', 'pydj.playlist.views.user_settings', {}, 'user_settings'),
(r'^keygen/?$', 'pydj.playlist.views.keygen', {}, 'keygen'),
(r'^g2admin$', 'pydj.playlist.views.g2admin', {}, 'g2admin'), 
(r'^stop_stream$', 'pydj.playlist.views.stop_stream', {}, 'stop_stream'), 
(r'^start_stream$', 'pydj.playlist.views.start_stream', {}, 'start_stream'), 

#javascript stuff
(r'^artist/$', 'pydj.playlist.views.artist', {}, "artist_js"),
(r'^song/$', 'pydj.playlist.views.song', {}, "song_js"),
(r'^user/$', 'pydj.playlist.views.user', {}, "user_js"),
(r'^playlist/remove/$', 'pydj.playlist.views.removeentry', {}, "removeentry_js"), 

#(r'', 'django.contrib.auth.views.redirect_to_login', {'next': 'playlist'}),




)
