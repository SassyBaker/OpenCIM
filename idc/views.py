from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from .models import Quantity


# Create your views here.
class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = '__all__'


class QuantityListView(generics.ListAPIView):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    permission_classes = [permissions.IsAdminUser]
