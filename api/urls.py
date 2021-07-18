from django.urls import path
from .views import *


urlpatterns = [
    path("get/", LaptopListView.as_view(), name="api-laptops"),
    path("create/", LaptopCreateView.as_view(), name="api-laptopcreate"),
    path("get/<pk>/", LaptopRetrieveView.as_view(), name="api-laptopretrieve"),
    path("update/<pk>/", LaptopUpdateView.as_view(), name="api-laptopupdate"),
    path("delete/<pk>/", LaptopDeleteView.as_view(), name="api-laptopdelete"),
]
