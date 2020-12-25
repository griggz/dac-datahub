from rest_framework import generics, pagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from leads.models import ContactUs
from leads.api.serializers import ContactUsSerializer
from leads.api.pagination import GeneralPagination


class ContactUsRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class ContactUsListCreate(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = GeneralPagination

    def perform_create(self, serializer):
        serializer.save()
