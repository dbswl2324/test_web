from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return render(request, 'analysisapp/show.html') 

def index(request):
    return render(request, 'analysisapp/index.html') 