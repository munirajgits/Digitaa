# from django.contrib.auth.models import User
from digitaastore.models import Laptops
from rest_framework import serializers


class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'
