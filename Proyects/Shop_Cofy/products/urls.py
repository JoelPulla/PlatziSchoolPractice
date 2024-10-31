
from django.urls import path
from .views import ProductFromView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="all_product"),
    path('agregar/', ProductFromView.as_view(), name="add_product"),
    
]
