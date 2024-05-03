from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nume complet'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Adresa de mail'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Adresa 1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Adresa 2'}), required=False)
    shipping_city = forms.CharField(label="",
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Oras'}),
                                    required=True)
    shipping_state = forms.CharField(label="",
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Județ'}),
                                     required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Cod postal'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Țara'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city',
                  'shipping_state', 'shipping_zipcode', 'shipping_country']

        exclude = ['user', ]


class PaymentForm(forms.Form):
    card_name = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele cardului'}),
                                required=True)
    card_number = forms.CharField(label="",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Numarul cardului'}),
                                  required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Data expirării'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'CVV'}), required=True)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Adresa de facturare 1'}), required=True)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Adresa de facturare 2'}), required=False)
    card_city = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Orasul de facturare'}),
                                required=True)
    card_state = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Județul de facturare'}), required=True)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Codul postal de facturare'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tara de facturare'}), required=True)
