from django.urls import path
from .views import QuantityListView


urlpatterns = [
    path('stock/', QuantityListView.as_view()),
    # path('stock/<str:product_sku>/', CableRetrieveUpdateView.as_view()),
    # path('api/auth/login/', CustomAuthToken.as_view()),
]
