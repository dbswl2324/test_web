from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CHOICE_CLASS

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    userclass = forms.IntegerField(label="고객등급", widget=forms.Select(choices=CHOICE_CLASS))

    class Meta:
        model = User
        fields  = ("username", "email","userclass")

class searchForm(forms.Form):
    search_item = forms.CharField(max_length=150)