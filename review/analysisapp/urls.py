from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'analysisapp'

urlpatterns = [
    path('show/', views.show, name='show'),
    path('index/', views.index, name='index'), 
]

