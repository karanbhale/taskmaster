from contactus import views
from django.urls import path


urlpatterns = [
    path('contactus',views.contact,name='contact'), #  this is url if we provide todolist in url then we visit to this app
   
]