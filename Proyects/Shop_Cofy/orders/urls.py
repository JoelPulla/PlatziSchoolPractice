from django.urls import path, include
from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path('myorder/', MyOrderView.as_view(), name="my_order"),
    path('add_product', CreateOrderProductView.as_view(), name="add_product")
     
] 