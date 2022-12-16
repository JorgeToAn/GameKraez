from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import CheckoutForm
from.models import (
    Product,
    Order,
    OrderProduct,
    CheckoutAddress, 
    Payment
)

# Create your views here.
class IndexPageView(TemplateView):
    template_name: str='index.html'