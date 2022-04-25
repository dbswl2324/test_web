from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'analysisapp'

urlpatterns = [
    path('show/', views.show, name='show'),
    path('index/', views.index, name='index'), 
    path('index/index/', views.index,), 
    path('index/search_main/', views.search_main,name='search_main'),
]

