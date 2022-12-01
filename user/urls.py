from django.urls import path
from .views import CustomerSignUpView, ManagerSignUpView, ManagerSignUpDoneView


urlpatterns = [
    path('signup/', CustomerSignUpView.as_view(), name='signup'),
    path('manager-signup/', ManagerSignUpView.as_view(), name='manager_signup'),
    path('manager-signup-done/', ManagerSignUpDoneView.as_view(), name='manager_signup_done'),
]