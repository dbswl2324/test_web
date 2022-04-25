from datetime import datetime
from django.shortcuts import render

# Create your views here.
from curses import raw
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from homeapp.forms import UserForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from homeapp.models import Member
from .forms import UserChange
from time import gmtime, strftime
from datetime import datetime

from homeapp.forms import UserChange

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
        search_name = request.POST.get('search-item')
        time = datetime.now()
        return HttpResponse((search_name, time))


def mypage(request):
    if request.method == "POST":
        userclass = request.POST.get('userclass')
        return HttpResponse(userclass)
    return render(request, 'homeapp/mypage.html')

# @login_message_required
def user_delete(request):
    request.user.delete()
    logout(request)
    context = {}
    return render(request, 'homeapp/user_delete.html', context)

def update(request, pk):
    if request.method == "POST":
        form = UserChange(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserChange(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'homeapp/user_update.html', context)

# class update(UpdateView):
#     model = Member
#     form_class = update
#     success_url = reverse_lazy('homeapp:user_update.html')
