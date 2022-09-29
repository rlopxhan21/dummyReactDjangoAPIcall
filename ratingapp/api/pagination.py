from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class VideoListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'record'
    page_size_query_param = 'urecord'
    max_page_size = 10
    # last_page_strings = ('end') last by default
    
class VideoListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class VideoListCPagination(CursorPagination):
    page_size = 4
    ordering = 'created'
    cursor_query_param = 'record'