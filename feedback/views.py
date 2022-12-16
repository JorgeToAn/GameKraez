from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Feedback
from user.models import User

# Create your views here.
class FeedbackListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name: str='feedback/list.html'
    model = Feedback

    def test_func(self):
        user = User.objects.filter(pk=self.request.user.id).get()
        return user.role == User.Role.MANAGER

class FeedbackDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    template_name: str='feedback/detail.html'
    model = Feedback

    def test_func(self):
        user = User.objects.filter(pk=self.request.user.id).get()
        return user.role == User.Role.MANAGER

class FeedbackCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name: str='feedback/new.html'
    model = Feedback
    fields = ['first_name', 'last_name', 'email', 'score', 'comment']

class FeedbackDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    template_name: str='feedback/delete.html'
    model = Feedback
    success_url = reverse_lazy('feedback_list')

    def test_func(self):
        user = User.objects.filter(pk=self.request.user.id).get()
        return user.role == User.Role.MANAGER