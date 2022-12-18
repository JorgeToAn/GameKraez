from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
from orders.models import Product

# Create your models here.
class Review(models.Model):
    SCORE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    score = models.IntegerField(choices=SCORE_CHOICES, default=1)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_review', args=[self.id])
