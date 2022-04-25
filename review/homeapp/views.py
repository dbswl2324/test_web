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
    if request.method == "POST":
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')
        # m = Member.objects.get(user_id = user_id, user_pw = user_pw)
        return redirect('index')
    else:
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
            login(request,)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, "homeapp/signup.html", {'form': form})

def test(request):
    if request.method == "POST":
        item = request.POST.get('search-item')
        return HttpResponse(item)
    return render(request, 'homeapp/test.html')
