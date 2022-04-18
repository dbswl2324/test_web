from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index1/', views.index1, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name="homeapp/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('board/', views.board),
]