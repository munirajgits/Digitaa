from django.db.models import *

# Create your models here.
class Laptops(Model):
    name=CharField(max_length=255, null=False, unique=True, blank=False)
    processor=CharField(max_length=255, null=False, blank=False)
    camera=CharField(max_length=255, null=False, blank=False)
    memory=CharField(max_length=255, null=False, blank=False)
    storage=CharField(max_length=255, null=False, blank=False)
    display=CharField(max_length=255, null=False, blank=False)
    price=FloatField()
    pics=ImageField(null=True, blank=True)