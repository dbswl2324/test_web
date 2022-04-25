from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from analysisapp.models import ArticleInfo, BuyList, ReviewData,ReviewAnalysis
# Create your views here.

def show(request):
    return render(request, 'analysisapp/show.html') 

def search_main(request):
      if request.method == "POST":
           search_name = request.POST.get('search_name')
           list = get_object_or_404(ArticleInfo, search_name=request.POST.get('search_name'))
           item = get_object_or_404(ReviewAnalysis, article_code=list.article_code)
           row = ReviewData.objects.filter(article_code=list.article_code)
           item2 = list.article_code
           item3=BuyList.objects.filter(article_code=list.article_code).order_by('buy_coin')
           return render(request, 'analysisapp/index.html', {'item': item,'item2':item2,'row':row,'item3':item3,'list':list})
      print("ffffffffffffff")
      return HttpResponseRedirect('/analysis/show/')


def index(request):
     if 'article_code' in request.GET:
         item = get_object_or_404(ReviewAnalysis, article_code=request.GET.get('article_code'))
         print("스탭 1")
         item2 = request.GET.get('article_code')
         row = ReviewData.objects.filter(article_code=request.GET.get('article_code'))
         list = get_object_or_404(ArticleInfo, article_code=request.GET.get('article_code'))
         item3=BuyList.objects.filter(article_code=request.GET.get('article_code')).order_by('buy_coin')
        
         return render(request, 'analysisapp/index.html', {'item': item,'item2':item2,'row':row,'item3':item3,'list':list})
     elif 'search_name' in request.POST:
          search_name = request.POST.get('search_name')
          list = get_object_or_404(ArticleInfo, search_name=request.POST.get('search_name'))
          item = get_object_or_404(ReviewAnalysis, article_code=list.article_code)
          row = ReviewData.objects.filter(article_code=list.article_code)
          item2 = list.article_code
          item3=BuyList.objects.filter(article_code=list.article_code).order_by('buy_coin')
          return render(request, 'analysisapp/index.html', {'item': item,'item2':item2,'row':row,'item3':item3,'list':list})
     print("asfasdafds")    
     return HttpResponseRedirect('/analysis/show')