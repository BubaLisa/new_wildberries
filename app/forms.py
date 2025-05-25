from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Пользователь с таким email не найден.")
            else:
                if not user.check_password(password):
                    raise forms.ValidationError("Неверный пароль.")
                if not user.is_active:
                    raise forms.ValidationError("Пользователь неактивен.")
                self.user = user
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)
