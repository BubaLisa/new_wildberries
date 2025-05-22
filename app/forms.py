from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    phone_number = forms.CharField(required=False, label="Номер телефона")
    address = forms.CharField(widget=forms.TextInput, required=False, label="Адрес")

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "address", "password1", "password2")
