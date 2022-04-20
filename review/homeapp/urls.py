from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name="homeapp/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('', views.search, name='search'),
    path('board/', views.board),
]