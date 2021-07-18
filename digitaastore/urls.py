from django.urls.conf import path
from .views import LaptopsListview

urlpatterns=[
    path('', LaptopsListview.as_view())
]