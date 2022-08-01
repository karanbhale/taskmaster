from django.core import paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import tasks
from .forms import tasklist
from django.contrib import messages
from django.core.paginator import Paginator
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def todolist(request):
    #working with jinja 2
    if request.method == 'POST':
        form = tasklist(request.POST or None)
        if form.is_valid():
    #  before saving it  connect it with its login user then save it
            form.save(commit=False).owner=request.user
            form.save()
        messages.success(request,message="Task added successfully...")
        return redirect('todolist')
    else:
        task = tasks.objects.filter(owner=request.user) #getting all objects of our tasks class
        paginators = Paginator(task,3)
        pages = request.GET.get('page')
        task = Paginator.get_page(paginators,pages) 
        context = {'tasks':task}
        return render(request,'todolist.html',context) # redirecting to the html file in template folder

@login_required
def delete_task(request,task_id):
    del_task = tasks.objects.get(pk=task_id)
    # del_task = tasks.objects.all().delete()
    if del_task.owner == request.user:
        del_task.delete()
    else:
        messages.error(request,message="Access denied for deleting this task...")
        
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == 'POST':
        task_obj = tasks.objects.get(pk=task_id)
        form = tasklist(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
            
        messages.success(request,message="Task edited successfully...")
        return redirect('todolist')
    else:
        task_obj = tasks.objects.get(pk=task_id) #getting all objects of our tasks class
     
        context = {'task_obj':task_obj}
        return render(request,'edit.html',context)    


def about(request):
    #working with jinja 2
    context = {'welcome_text': 'welcome to about'}
    return render(request,'about.html',context) # redirecting to the html file in template folder

def index(request):
    #working with jinja 2
    context = {'welcome_text': 'welcome to index page '}
    return render(request,'index.html',context) # redirecting to the html file in template folder
