from django import forms
from .models import Product, Customer

class ProductForm(forms.ModelForm):
    name=forms.CharField(required=True, label="Product Name:",widget=forms.TextInput(
        attrs={
        "placeholder": "Enter Product Name"

    }))
    price= forms.FloatField(required=True,label="Product Price:",widget=forms.TextInput(
        attrs={
        "placeholder": "Enter price"
    }))
    class Meta:
        model= Product
        fields='__all__'