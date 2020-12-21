import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, pagination, authentication, exceptions, status
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
# from .tasks import email_new_user, email_admins
from rest_framework.decorators import (api_view,
                                       permission_classes, authentication_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from dataHub.settings import SECRET_KEY
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from accounts.models import User
from .serializers import (AuthSerializer, AuthSerializerDetail, UserCreateSerializer)


@api_view(["POST"])
@permission_classes([AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    return Response(HTTP_201_CREATED)


# This api is used to id the accountName of the logged in user
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def fetch_account(request):
    user = request._user
    obj = User.objects.get(email=user)
    meta = json.loads(obj.meta)

    return Response({
        "email": obj.email,
        "is_admin": obj.is_admin,
        "nickname": obj.nickname,
        "first_name": obj.first_name,
        "last_name": obj.last_name,
        "slug": obj.slug,
        "groups": obj.groups.values(),
        'meta': meta
        })


class AuthPageNumberPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):
        user = False
        sys_user = self.request.user
        meta = self.request.META
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


# Metrics API: Primary view showing ALL data grouped by overarching State.
class AuthAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AuthPageNumberPagination


class AuthDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializerDetail
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
