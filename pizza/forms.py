from django import forms
from .models import OrderModel
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model=OrderModel
        fields="__all__"

        labels={
            "pizzaName":"Pizza",
            "size":"Size of pizza",
            "city":"Type city",
            "houseNumber":"Residention Number",
            "email":"Email",
            "phoneNumber":"Phone number"
        }
