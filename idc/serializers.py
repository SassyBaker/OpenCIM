from rest_framework import serializers
from .models import CableInventory


class AllCableDetails(serializers.ModelSerializer):
    class Meta:
        model = CableInventory
        fields = (
            'cable',
            'cable_name',
            'sku',
            'quantity',
            'on_order',
        )


# class AllCableDetails(serializers.ModelSerializer):
#     class Meta:
#         model = CableInventory
#         fields = '__all__'
