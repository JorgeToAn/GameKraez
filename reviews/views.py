from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Review
from orders.models import Product
# Create your views here.
class PostDetailView(DetailView):
    template_name = 'review/detail.html'
    model = Review

class PostPublishedView(LoginRequiredMixin, ListView):
    template_name = 'review/list.html'
    model = Review

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(
                                    author=self.request.user
                                    ).order_by(
                                        'created_on').reverse()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "review/new.html"
    model = Review
    fields = ["title", "subtitle", "body", "score"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['productId'])
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "review/edit.html"
    model = Review
    fields = ["title", "subtitle", "body", "score"]

    def test_func(self):
        review_obj = self.get_object()
        return review_obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "review/delete.html"
    model = Review
    success_url = reverse_lazy("catalog")

    def test_func(self):
        review_obj = self.get_object()
        return review_obj.author == self.request.user
