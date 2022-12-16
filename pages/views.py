from django.views.generic import TemplateView
from orders.models import Product

# Create your views here.
class IndexPageView(TemplateView):
    template_name: str='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.all()[:4]
        return context