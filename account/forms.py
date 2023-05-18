from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('niepoprawne dane logowania')
        cleaned_data['user'] = user
        return cleaned_data


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Haslo')
    password2 = forms.CharField(widget=forms.PasswordInput, label='re-haslo')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('hasla nie sa jednakowe')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email']
