from digitaastore.models import Laptops
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class LaptopsListview(ListView):
    queryset=Laptops.objects.all()
    template_name='digitaastore/laptops.html'
