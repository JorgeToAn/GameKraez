from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ManagerCreationForm, CustomerCreationForm
from .models import User, Customer

# Create your views here.
class CustomerSignUpView(CreateView):
    template_name: str='registration/signup.html'
    form_class = CustomerCreationForm
    model = Customer
    success_url = reverse_lazy('login')