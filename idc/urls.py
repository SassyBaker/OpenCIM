from django.urls import path
from .views import ListCableInventory, DetailCableInventory

urlpatterns = [
    path('cable/stock/', ListCableInventory.as_view()),
    path('cable/stock/<str:product_sku>/', DetailCableInventory.as_view()),
]
