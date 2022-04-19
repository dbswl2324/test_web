from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from analysisapp.models import ReviewAnalysis
# Create your views here.

def show(request):
    return render(request, 'analysisapp/show.html') 

# def index(request):
#     return render(request, 'analysisapp/index.html') 

def index(request):
    if 'article_code' in request.GET:
        item = get_object_or_404(ReviewAnalysis, article_code=request.GET.get('article_code'))
        return render(request, 'analysisapp/index.html', {'item': item})
    return HttpResponseRedirect('/analysis/index/')