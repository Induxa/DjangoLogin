from django import forms


class Login(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'login_name', 'placeholder': 'Введите логин', 'name': 'login'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login_password', 'placeholder': 'Введите пароль', 'name': 'password'}))
