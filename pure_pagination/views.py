from datetime import datetime, timedelta

from django.shortcuts import redirect
from django.conf import settings
from pure_pagination.paginator import ITEMS_PER_PAGE_REDIRECT_VIEW_NAME, ITEMS_PER_PAGE_COOKIE_NAME


def set_ipp_limit(request, limit):
    if not ITEMS_PER_PAGE_REDIRECT_VIEW_NAME:
        raise KeyError('Set ITEMS_PER_PAGE_REDIRECT_VIEW_NAME parameter')
    response = redirect(ITEMS_PER_PAGE_REDIRECT_VIEW_NAME)
    cookie_expires = datetime.now() + timedelta(365*10)
    response.set_cookie(ITEMS_PER_PAGE_COOKIE_NAME, value=limit, expires=cookie_expires, path='/', httponly=True)
    return response
