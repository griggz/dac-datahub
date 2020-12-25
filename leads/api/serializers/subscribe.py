from rest_framework import serializers
from leads.models import Subscribe
import json

class SubscribeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='leads-api:subscribe-record',
        lookup_field='id'
    )

    class Meta:
        model = Subscribe
        fields = (
            'email',
            'date_created',
            'url'
        )

        @staticmethod
        def create(validated_data):
            return Subscribe.objects.create(**validated_data)
