from django.urls import path
from .views import (
    IndexPageView,
    ProductView,
    HomeView,
    OrderSummaryView,
    CheckoutView,
    PaymentView
)




urlpatterns=[
    path('', IndexPageView.as_view(), name='index'),
    path('', ProductView.as_view(), name='product'),
    path('', HomeView.as_view(), name='home'),
    path('', OrderSummaryView.as_view(), name='order_summary'),
    path('', CheckoutView.as_view(), name='checkout'),
    path('', PaymentView.as_view(), name='payment')
]