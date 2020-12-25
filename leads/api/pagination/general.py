from rest_framework import generics, pagination
from rest_framework.response import Response


class GeneralPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):

        sys_user = self.request.user
        if sys_user.is_authenticated:
            user = True

        if sys_user.is_staff:
            staff = True
        else:
            staff = False

        context = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'user': user,
            'staff': staff,
            'results': data,
        }
        return Response(context)