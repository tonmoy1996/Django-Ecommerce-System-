from django import forms
from .models import Product, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class UserCreation(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
