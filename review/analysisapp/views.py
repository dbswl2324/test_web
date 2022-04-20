from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from analysisapp.models import ArticleInfo, BuyList, ReviewData,ReviewAnalysis
# Create your views here.

def show(request):
    return render(request, 'analysisapp/show.html') 

#def index(request):
#    return render(request, 'analysisapp/index.html') 

def index(request):
     if 'article_code' in request.GET:
         item = get_object_or_404(ReviewAnalysis, article_code=request.GET.get('article_code'))
         
         item2 = ReviewData.objects.all()
         row = ReviewData.objects.filter(article_code=request.GET.get('article_code'))

         item3=BuyList.objects.filter(article_code=request.GET.get('article_code')).order_by('buy_coin')
         
         return render(request, 'analysisapp/index.html', {'item': item,'item2':item2,'row':row,'item3':item3})
     return HttpResponseRedirect('/analysis/index/')