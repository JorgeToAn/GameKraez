from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import CatalogView, CartView, ProductDetailView, updateItem, processOrder

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
]

# Loads the media directory to display the product images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)