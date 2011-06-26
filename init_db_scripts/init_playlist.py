#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript playlist

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
import os

def run():
    from pydj.playlist.models import SongDir

    directory = os.path.join(settings.PROJECT_PATH, 'playlist/song_dir');
    if not os.path.exists(directory):
        print "Directory %s doesn't exists, please create." %directory
        return

    playlist_songdir_1 = SongDir()
    playlist_songdir_1.path = directory
    playlist_songdir_1.hash_letters = 0L
    playlist_songdir_1.usable = True
    playlist_songdir_1.save()

    from pydj.playlist.models import Settings

    playlist_settings_1 = Settings()
    playlist_settings_1.key = u'welcome_message'
    playlist_settings_1.value = u'0'
    playlist_settings_1.save()

