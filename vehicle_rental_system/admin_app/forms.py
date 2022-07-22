from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from admin_app.models import UserInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =('username', 'first_name', 'last_name','email', 'password')