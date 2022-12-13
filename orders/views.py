from django.views.generic import ListView, DetailView, UpdateView, DeleteView, View
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Product, 
    Order, 
    OrderProduct
)

# Create your views here.
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

class CatalogView(ListView):
    template_name: str='products/catalog.html'
    paginate_by = 10
    model = Product

    def get_queryset(self):
        name = self.request.GET.get('name')
        category = self.request.GET.get('category')
        order_price = self.request.GET.get('order')
        
        query = Product.objects.all()
        if name:
            query = query.filter(product_name__icontains=name)
        if category:
            query = query.filter(category__icontains=category)
        if order_price:
            query = query.order_by(order_price)
        return query

class ProductDetailView(DetailView):
    template_name: str='products/detail.html'
    model = Product