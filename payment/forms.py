from django.db.models.functions import Now
from django import forms
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import CheckoutAddress, Payment

# class CheckoutForm(forms.Form):
#     street_address = forms.CharField(widget=forms.TextInput(attrs={
#         'class':'form-control',
#         'placeholder': 'Apartment or suite'
#     }))
#     country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
#         'class':'custom-select d-block w-100'
#     }))
#     zip = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     same_billing_address = forms.BooleanField(required=False)
#     save_info = forms.BooleanField(required=False)

class CheckoutForm(ModelForm):
    class Meta:
        model = CheckoutAddress
        fields = ['street_address', 'apartment_address', 'city', 'country', 'zip']

# class PaymentForm(ModelForm):
#     class Meta:
#         model = Payment
#         fields = []
    
#     def __init__(self, *args, **kwargs):
#         super(PaymentForm, self).__init__(*args, **kwargs)
#         self.fields['transaction_id'] = f"P-{Now()}"