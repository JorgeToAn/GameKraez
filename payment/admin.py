from django.contrib import admin

# Register your models here.
from .models import CheckoutAddress, Payment

admin.site.register(CheckoutAddress)
admin.site.register(Payment)