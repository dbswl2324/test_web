from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    userclass = forms.ChoiceField(label="고객등급")

    class Meta:
        model = User
        fields  = ("email", "userclass")