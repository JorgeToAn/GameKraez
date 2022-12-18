from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm

# Create your views here.
@login_required
def checkout(request):
    context = {}
    context['form'] = CheckoutForm
    return render(request, 'payment/checkout.html', context)