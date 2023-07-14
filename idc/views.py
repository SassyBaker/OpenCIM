from rest_framework import generics
from .models import CableInventory
from .serializers import AllCableDetails


# Create your views here.
class ListCableInventory(generics.ListAPIView):
    queryset = CableInventory.objects.all()
    serializer_class = AllCableDetails


class DetailCableInventory(generics.RetrieveUpdateAPIView):
    queryset = CableInventory.objects.all()
    serializer_class = AllCableDetails
    lookup_field = 'sku'
    lookup_url_kwarg = 'product_sku'
