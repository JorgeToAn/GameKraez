from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer


class ManagerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']