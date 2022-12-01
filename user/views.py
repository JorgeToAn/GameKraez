from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ManagerCreationForm, CustomerCreationForm
from .models import User, Customer

# Create your views here.
class CustomerSignUpView(CreateView):
    template_name: str='registration/signup.html'
    form_class = CustomerCreationForm
    model = Customer
    success_url = reverse_lazy('login')

class ManagerSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name: str='registration/manager_signup.html'
    form_class = ManagerCreationForm
    model = User
    success_url = reverse_lazy('manager_signup_done')

    def test_func(self):
        user = User.objects.filter(pk=self.request.user.id).get()
        return user.role == User.Role.MANAGER

class ManagerSignUpDoneView(TemplateView):
    template_name: str='registration/manager_signup_done.html'