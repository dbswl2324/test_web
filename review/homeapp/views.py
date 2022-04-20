from django.shortcuts import render

# Create your views here.
from curses import raw
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from homeapp.forms import UserForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

app_name = 'homeapp'

def index(request):
    return render(request, "homeapp/index.html")
# Create your views here.

def board(request):
    return render(request, "homeapp/board.html")

def login(request):
    return render(request, "homeapp/login.html")

@require_http_methods(["GET", "POST"])
@csrf_exempt
def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, "homeapp/signup.html", {'form': form})

# def search(request):
    # item = request.GET.get('search-item')
    # context = {
    #     'item': item
    # }
    # return render(request, 'analysis/index.html', context) 
    # if request.method == "GET":
    #     searched = request.GET['searched']
    #     return render(request, 'searched.html', {'searched':searched})
    # else:
    #     return render(request, 'searched.html', {})