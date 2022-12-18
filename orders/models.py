from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.urls import reverse
from payment.models import CheckoutAddress, Payment

# Validators
def validate_price(value):
    if value <= 0:
        raise ValidationError(
        _('Price below or equal to zero is not allowed'),
        code='invalid')

def validate_quantity(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a valid quantity'),
            code='invalid',
            params={value})

# Create your models here.
class Product(models.Model):
    CATEGORY = [
        ('COMPUTER', 'Computer'),
        ('ELECTRONICS', 'Electronics'),
        ('GAMING', 'Gaming'),
        ('OFFICE', 'Office'),
        ('NETWORKING', 'Networking'),
        ('THEATER', 'Theater'),
        ('TOYS', 'Toys'),
        ('SOFTWARE', 'Software'),
        ('AUDIO_VIDEO', 'Audio & Video'),
    ]

    product_name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[validate_price])
    category = models.CharField(choices=CATEGORY, max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product', args=[self.id])

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(CheckoutAddress, on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True, blank=True)
    ordered = models.BooleanField(default=False)

    @property
    def get_subtotal(self):
        orderproducts = self.orderproduct_set.all()
        subtotal = sum([orderproduct.get_total for orderproduct in orderproducts])
        return subtotal
    
    @property
    def get_tax(self):
        orderproducts = self.orderproduct_set.all()
        tax = float(sum([orderproduct.get_total for orderproduct in orderproducts])) * 0.08
        return round(tax, 2)
    
    @property
    def get_total(self):
        subtotal = float(self.get_subtotal)
        tax = self.get_tax
        total = subtotal + tax
        return total
    
    @property
    def get_quantity(self):
        orderproducts = self.orderproduct_set.all()
        quantity = sum([orderproduct.quantity for orderproduct in orderproducts])
        return quantity

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.ordered_date}"

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, validators=[validate_quantity])
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"