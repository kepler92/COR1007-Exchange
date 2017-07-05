from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='name', max_length=30)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    password_check = forms.CharField(label='password_check', widget=forms.PasswordInput())