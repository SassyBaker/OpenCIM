from django.db import models
from core.models import Cable


# Create your models here.
class Quantity(models.Model):
    name = models.ForeignKey(Cable, on_delete=models.DO_NOTHING)

    # In Stock
    previous_quantity = models.PositiveIntegerField(editable=False, default=0)
    quantity = models.PositiveIntegerField()

    # Incoming Stock
    previous_on_order = models.PositiveIntegerField(editable=False, default=0)
    on_order = models.PositiveIntegerField()

    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.name)
