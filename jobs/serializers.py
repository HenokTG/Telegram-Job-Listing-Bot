from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import JobListings


class JobListingBotSerializer(ModelSerializer):

    class Meta:
        model = JobListings
        fields = '__all__'
        depth = 1
