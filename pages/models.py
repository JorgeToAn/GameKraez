from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
CATEGORY = (

)
class Product(models.Model):
    product_name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image = models.ForeignKey(
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.Charfield(choices=CATEGORY, max_length=2)
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
    quantity = models.IntegerField(default=1)


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