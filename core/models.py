from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# The main user model with customizations
class User(AbstractUser):
    email = models.EmailField(unique=True)


class Cable(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)

    # Parent
    cable_type = models.ForeignKey('Type', on_delete=models.CASCADE)
    cable_color = models.ForeignKey('Color', on_delete=models.CASCADE)
    cable_length = models.ForeignKey('Length', on_delete=models.CASCADE)
    connector = models.ForeignKey('Connector', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = f"{self.brand} {self.cable_type} {self.connector} ({self.cable_length})"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


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
