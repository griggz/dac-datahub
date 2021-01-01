from rest_framework import generics, pagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from leads.models import Subscribe
from leads.api.serializers import SubscribeSerializer
from leads.api.pagination import GeneralPagination


class SubscribeRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class SubscribeListCreate(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [AllowAny]
    pagination_class = GeneralPagination

    def perform_create(self, serializer):
        serializer.save()