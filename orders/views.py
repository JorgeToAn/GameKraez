from django.db.models.functions import Now
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Product, Order, OrderProduct
from payment.models import CheckoutAddress, Payment
import datetime
import json

class CatalogView(ListView):
    template_name: str='products/catalog.html'
    paginate_by = 10
    model = Product

    def get_queryset(self):
        q = self.request.GET.get('q')
        name = self.request.GET.get('name')
        category = self.request.GET.get('category')
        order_price = self.request.GET.get('order')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        
        query = Product.objects.all()
        if q:
            query = query.filter(product_name__icontains=q)
        if name:
            query = query.filter(product_name__icontains=name)
        if category:
            query = query.filter(category__icontains=category)
        if min and max:
            query = query.filter(price__range=(min, max))
        if order_price:
            query = query.order_by(order_price)
        return query

class ProductDetailView(DetailView):
    template_name: str='products/detail.html'
    model = Product

class CartView(LoginRequiredMixin, TemplateView):
    template_name: str='products/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(user=self.request.user, ordered=False)
        context['order'] = order
        context['items'] = order.orderproduct_set.all()

        return context

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(pk=productId)
    order, created = Order.objects.get_or_create(
        user=customer,
        ordered=False
    )
    orderProduct, created = OrderProduct.objects.get_or_create(
        product=product,
        order=order
    )

    if action == 'add':
        orderProduct.quantity = (orderProduct.quantity + 1)
    elif action == 'remove':
        orderProduct.quantity = (orderProduct.quantity - 1)
    elif action == 'delete':
        orderProduct.quantity = 0
    
    orderProduct.save()

    if orderProduct.quantity <= 0:
        orderProduct.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        customer = request.user
        data_shipping = data['shipping']
        transaction_id = f"{customer.username[:10]}-{datetime.datetime.now().timestamp()}"

        order, created = Order.objects.get_or_create(user=customer, ordered=False)
        
        payment = Payment.objects.create(transaction_id=transaction_id)

        shipping, created = CheckoutAddress.objects.get_or_create(
            street_address=data_shipping['street_address'],
            apartment_address=data_shipping['apartment_address'],
            city=data_shipping['city'],
            country=data_shipping['country'],
            zip=data_shipping['zip']
        )

        order.address = shipping
        order.payment = payment
        order.ordered_date = datetime.datetime.now()
        order.ordered = True
        order.save()
        return JsonResponse('Payment confirmed', safe=False)
    else:
        return JsonResponse('Payment failed', safe=False)
