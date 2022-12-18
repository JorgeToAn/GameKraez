from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


# Create your models here.
class CheckoutAddress(models.Model):
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_address} {self.zip} in {self.country}"

class Payment(models.Model):
    transaction_id = models.CharField(max_length=50, default='DEFAULT')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} at {self.timestamp}"