from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Review, Status
# Create your views here.
class PostDetailView(DetailView):
    template_name = 'review/detail.html'
    model = Review

class PostPublishedView(ListView):
    template_name = 'review/list.html'
    model = Review

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="published")
        context['review_list'] = Review.objects.filter(
                                    author=self.request.user
                                    ).filter(status=pending_status).order_by(
                                        'created_on').reverse()
        return context 

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "review/new.html"
    model = Review
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "review/edit.html"
    model = Review
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        review_obj = self.get_object()
        return review_obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = "review/delete.html"
    model = Review
    success_url = reverse_lazy("list")

    def test_func(self):
        review_obj = self.get_object()
        return review_obj.author == self.request.user
