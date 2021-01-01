from rest_framework import serializers
from leads.models import ContactUs
import json

class ContactUsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='leads-api:contact_us-record',
        lookup_field='id'
    )

    class Meta:
        model = ContactUs
        fields = (
            'url',
            'first_name',
            'last_name',
            'email',
            'job_title',
            'organization',
            'work_phone',
            'web_site',
            'number_of_staff',
            'industry',
            'solution_option',
            'contact_date',
            'method_of_referral',
            'contact_source',
            'additional_details'
        )

        @staticmethod
        def create(validated_data):
            return ContactUs.objects.create(**validated_data)
