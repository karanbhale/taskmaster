from todolist import views
from django.urls import path

urlpatterns = [
    path('',views.todolist,name='todolist'), #  this is url if we provide todolist in url then we visit to this app
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
  
]