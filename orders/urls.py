from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import CatalogView, ProductDetailView

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]

# Loads the media directory to display the product images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)