#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript forum

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from forum.models import Category

    forum_category_1 = Category()
    forum_category_1.name = u'Radio'
    forum_category_1.sort_order = 0
    forum_category_1.save()

    from forum.models import Forum

    forum_forum_1 = Forum()
    forum_forum_1.title = u'Radio forum'
    forum_forum_1.slug = u'radio-forum'
    forum_forum_1.parent = None
    forum_forum_1.description = u'Stuff about the radio.'
    forum_forum_1.threads = 0
    forum_forum_1.posts = 0
    forum_forum_1.category = forum_category_1
    forum_forum_1.anonymous = False
    forum_forum_1.sort_order = 0
    forum_forum_1.save()

    from forum.models import Thread


    from forum.models import Post


    from forum.models import Subscription


    from forum.models import LastRead

