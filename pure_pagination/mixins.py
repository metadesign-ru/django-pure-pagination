# encoding: utf-8
from pure_pagination.paginator import (Paginator, ITEMS_PER_PAGE_COOKIE_NAME,
                                       ITEMS_PER_PAGE_DEFAULT, ITEMS_PER_PAGE_CHOICES)


class PaginationMixin(object):
    """
    Mixin for generic class-based views (e.g. django.views.generic.ListView)
    """
    # Replace the default django.core paginator by pure_pagination.Paginator
    paginator_class = Paginator

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        # Pass the request object to the paginator to keep the parameters in the url querystring ("?page=2&old_param=...")
        request = self.request
        return self.paginator_class(queryset, per_page, orphans=orphans, allow_empty_first_page=allow_empty_first_page, request=request)

    def get_paginate_by(self, queryset):
        # NOTE: сделать проверку на переопределение свойства paginate_by и кидать ошибку, что нельзя этого делать, потому что юзается django-pure-pagination и что нужно юзать переопределение через settings
        cookie_ipp = int(self.request.COOKIES.get(ITEMS_PER_PAGE_COOKIE_NAME, 0))
        return cookie_ipp if cookie_ipp in ITEMS_PER_PAGE_CHOICES else ITEMS_PER_PAGE_DEFAULT

    def get_context_data(self, **kwargs):
        context = super(PaginationMixin, self).get_context_data(**kwargs)
        queryset = kwargs.pop('object_list', self.object_list)
        context['page_size'] = self.get_paginate_by(queryset)
        return context
