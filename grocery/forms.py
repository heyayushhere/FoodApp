# grocery/forms.py
from django import forms


# grocery/forms.py
from django import forms

class PerishableItemForm(forms.Form):
    name = forms.CharField(label='Item Name')
    expiration_date = forms.DateField(label='Expiration Date', widget=forms.DateInput(attrs={'type': 'date'}))
