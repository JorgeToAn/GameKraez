from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.urls import reverse

# Validators
def validate_price(value):
    if value <= 0:
        raise ValidationError(
        _('Price below or equal to zero is not allowed'),
        code='invalid')

def validate_quantity(value):
    if value == 0:
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
    image = models.ImageField(upload_to='uploads/products')
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[validate_price])
    category = models.CharField(choices=CATEGORY, max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product', args=[self.id])


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[validate_quantity])


    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total