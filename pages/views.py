from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import (
    Product, 
    Order, 
    OrderProduct
)

# Create your views here.
class IndexPageView(TemplateView):
    template_name: str='index.html'

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object' : order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "No orders found :(")
            return redirect("/")