from django.shortcuts import render

# Create your views here.
from curses import raw
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from homeapp.forms import UserForm
from django.views.decorators.http import require_http_methods

app_name = 'homeapp'

def index1(request):
    return render(request, "homeapp/index.html")
# Create your views here.

def board(request):
    return render(request, "homeapp/board.html")

def login(request):
    return render(request, "homeapp/login.html")

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index1')
    else:
        form = UserForm()
    return render(request, "homeapp/signup.html", {'form': form})