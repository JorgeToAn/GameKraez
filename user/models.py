from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = 'MANAGER', 'Manager'
        CUSTOMER = 'CUSTOMER', 'Customer'

    base_role = Role.MANAGER
    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=254)

    REQUIRED_FIELDS = ['role', 'email']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)

class Customer(User):
    base_role = User.Role.CUSTOMER
    customer = CustomerManager

    class Meta:
        proxy = True