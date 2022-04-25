from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        model = Member
        fields  = ["username", "password1", "password2", "email", "nickname", "userclass"]

class searchForm(forms.Form):
    search_item = forms.CharField(max_length=150)

class UserChange(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["nickname", "email", "userclass"]