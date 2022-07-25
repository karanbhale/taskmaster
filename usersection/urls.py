from usersection import views
from django.urls import path
from django.contrib.auth import views as login_view


urlpatterns = [
    path('register',views.register,name='register'), #  this is url if we provide todolist in url then we visit to this app
    path('login',login_view.LoginView.as_view(template_name='login.html'),name='login'), #  this is url if we provide todolist in url then we visit to this app
    path('logout',login_view.LogoutView.as_view(template_name='logout.html'),name='logout'), #  this is url if we provide todolist in url then we visit to this app

]