from django.db import models
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
  class PropertyType(models.TextChoices):
    APARTMENT = 'apartment', _('Apartment')
    HOUSE = 'house', _('House')
    VILLA = 'villa', _('Villa')
    LAND = 'land', _('Land')

  class Status(models.TextChoices):
    AVAILABLE = 'available', _('Available')
    SOLD = 'sold', _('Sold')
    RENTED = 'rented', _('Rented')

  title = models.CharField(max_length=255)
  description = models.TextField()
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=12, decimal_places=2)
  type = models.CharField(max_length=50, choices=PropertyType.choices)
  status = models.CharField(max_length=50, choices=Status.choices, default=Status.AVAILABLE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title