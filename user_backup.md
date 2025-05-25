#models

class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        max_length=20,
        blank=True,
        null=True,
    )
    address = models.TextField(
        verbose_name="Адрес",
        max_length=300,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username




#views

def registration_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/registration_page.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app/index.html')  # или куда хочешь после логина
    else:
        form = AuthenticationForm()
    return render(request, 'app/login_page.html', {'form': form})




#settings

AUTH_USER_MODEL = 'app.User'



#forms
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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



#admin
from .models import Product, Category, Brand, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass



#urls

    path('registration/', views.registration_page, name='registration_page'),
    path('login/', views.login_page, name='login_page'),



#header

            <div class="nav-link"><a href="{% url 'login_page' %}">Вход</a></div>
            <div class="nav-link"><a href="{% url 'registration_page' %}">Регистрация</a></div>


#register_page

{% extends "base.html" %}

{% block content %}
<div class="registration-page">
    <h1>Регистрация</h1>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            {{ form.username.label_tag }}<br>
            {{ form.username }}
        </div>
        <div class="form-group">
            {{ form.email.label_tag }}<br>
            {{ form.email }}
        </div>
        <div class="form-group">
            {{ form.phone_number.label_tag }}<br>
            {{ form.phone_number }}
        </div>
        <div class="form-group">
            {{ form.address.label_tag }}<br>
            {{ form.address }}
        </div>
        <div class="form-group">
            {{ form.password1.label_tag }}<br>
            {{ form.password1 }}
        </div>
        <div class="form-group">
            {{ form.password2.label_tag }}<br>
            {{ form.password2 }}
        </div>
        <button type="submit" class="price-button">Зарегистрироваться</button>
    </form>
</div>
{% endblock %}




#login_page


{% extends "base.html" %}

{% block content %}
<div class="login-page">
    <h1>Вход</h1>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            {{ form.username.label_tag }}<br>
            {{ form.username }}
        </div>
        <div class="form-group">
            {{ form.password.label_tag }}<br>
            {{ form.password }}
        </div>
        <button type="submit" class="price-button">Войти</button>
    </form>
</div>
{% endblock %}