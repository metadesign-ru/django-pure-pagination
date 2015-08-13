# -*- coding: utf8 -*-
from django.conf import settings
from django.conf.urls import patterns, url

from pure_pagination import views
from pure_pagination.paginator import ITEMS_PER_PAGE_CHOICES


allowed_limitations = '|'.join([str(i) for i in ITEMS_PER_PAGE_CHOICES])

urlpatterns = patterns('',
    url(r'^ipp-limit-(?P<limit>(%s))/$' % allowed_limitations, views.set_ipp_limit, name='ipp_limit'),
)
