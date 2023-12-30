from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Adjust this according to your preference
    page_size_query_param = 'page_size'
    max_page_size = 100
