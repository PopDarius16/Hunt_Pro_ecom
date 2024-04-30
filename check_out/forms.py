from django import forms
from .models import CheckOut


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ['item', 'return_date']
