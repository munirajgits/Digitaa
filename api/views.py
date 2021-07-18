from django.shortcuts import render
from digitaastore.models import Laptops
from .serializers import LaptopsSerializer
from rest_framework.generics import *


# Create your views here.
class LaptopListView(ListAPIView):
    queryset=Laptops.objects.all()
    serializer_class=LaptopsSerializer

class LaptopCreateView(ListCreateAPIView):
    queryset=Laptops.objects.all()
    serializer_class=LaptopsSerializer

class LaptopRetrieveView(RetrieveAPIView):
    queryset=Laptops.objects.all()
    serializer_class=LaptopsSerializer

class LaptopUpdateView(RetrieveUpdateAPIView):
    queryset=Laptops.objects.all()
    serializer_class=LaptopsSerializer


class LaptopDeleteView(RetrieveDestroyAPIView):
    queryset=Laptops.objects.all()
    serializer_class=LaptopsSerializer
