from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/', views.index, name="index"),
    # path('', views.index),
    # path('login/', auth_views.LoginView.as_view(template_name="homeapp/login.html"), name="login"),
    path('login/', views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('board/', views.board),
    path('test/', views.test, name="test"), 
    path('mypage/', views.mypage, name="mypage"),
    path('user_delete/', views.user_delete, name="user_delete"),
    path('user_update/<int:pk>/', views.update, name='user_update'),
    # path('<str:param>/', views.urlpattern),
]