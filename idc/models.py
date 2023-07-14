from django.contrib.auth.models import User
from django.db import models


# Child of Central-->Model-->Cable
class CableInventory(models.Model):
    cable = models.ForeignKey('central.Cable', on_delete=models.DO_NOTHING)
    cable_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)

    # In Stock
    previous_quantity = models.PositiveIntegerField(editable=False)
    quantity = models.PositiveIntegerField()

    # Incoming Stock
    previous_on_order = models.PositiveIntegerField(editable=False)
    on_order = models.PositiveIntegerField()

    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)

        if not self.pk:
            # Object is new, so we don't have a history yet
            self.previous_quantity = 0
            self.previous_on_order = 0
            self.sku = self.cable.sku
            self.cable_name = self.cable.name

            super().save(*args, **kwargs)
        else:
            CableInventoryEditHistory.objects.create(
                parent=CableInventory.objects.get(id=self.pk),
                original_quantity=self.previous_quantity,
                updated_quantity=self.quantity,
                original_on_order_quantity=self.previous_on_order,
                updated_on_order_quantity=self.on_order,
                edited_by=request.user,
            )

            self.previous_quantity = self.quantity
            self.previous_on_order = self.on_order
            self.sku = self.cable.sku
            self.cable_name = self.cable.name

            super().save(*args, **kwargs)

    def __str__(self):
        return self.cable.name


class CableInventoryEditHistory(models.Model):
    parent = models.ForeignKey(CableInventory, on_delete=models.CASCADE)

    original_quantity = models.CharField(max_length=64)
    updated_quantity = models.CharField(max_length=64)

    original_on_order_quantity = models.CharField(max_length=64)
    updated_on_order_quantity = models.CharField(max_length=64)

    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent} --> {self.datetime}"
