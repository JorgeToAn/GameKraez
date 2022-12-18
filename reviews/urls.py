from django.urls import path
from .views import PostCreateView, PostDetailView, PostDeleteView, PostPublishedView, PostUpdateView

urlpatterns = [
    path('new/<int:productId>', PostCreateView.as_view(), name='create_review'),
    path('list/', PostPublishedView.as_view(), name='list_review'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail_review'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_review'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update_review'),
]