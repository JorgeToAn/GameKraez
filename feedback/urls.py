from django.urls import path
from .views import FeedbackListView, FeedbackDetailView, FeedbackCreateView, FeedbackDeleteView

urlpatterns = [
    path('', FeedbackListView.as_view(), name='feedback_list'),
    path('<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('new/', FeedbackCreateView.as_view(), name='feedback_new'),
    path('<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback_delete'),
]