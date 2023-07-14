from django.db import models
from django.contrib.auth.models import User


# Collection of cables used in DC
class Cable(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)

    # Parent
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    cable_type = models.ForeignKey("Type", on_delete=models.CASCADE)
    cable_color = models.ForeignKey("Color", on_delete=models.CASCADE)
    cable_length = models.ForeignKey("Length", on_delete=models.CASCADE)
    connector = models.ForeignKey("Connector", on_delete=models.CASCADE)

    # purchase_price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.name = f"{self.brand} {self.cable_color} {self.cable_type} {self.connector} ({self.cable_length})"

        request = kwargs.pop('request', None)

        if self.pk:
            EditHistory.objects.create(
                parent=Cable.objects.get(id=self.pk),
                edited_by=request.user,
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Future Edit: Add what was changed
class EditHistory(models.Model):
    parent = models.ForeignKey(Cable, on_delete=models.CASCADE)

    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent} --> {self.datetime}"


class Type(models.Model):
    type = models.CharField(max_length=64)
    def __str__(self): return self.type


class Color(models.Model):
    color = models.CharField(max_length=64)
    def __str__(self): return self.color


class Length(models.Model):
    length = models.CharField(max_length=64)
    def __str__(self): return self.length


class Connector(models.Model):
    connector = models.CharField(max_length=64)
    def __str__(self): return self.connector


class Brand(models.Model):
    brand = models.CharField(max_length=64)
    def __str__(self): return self.brand

