from django.shortcuts import render,redirect
from .forms import Customragistrationfrom
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = Customragistrationfrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,message="New Account Created!!!! login to continue")
            redirect('register')
    
    register_form = Customragistrationfrom()
    context = {'message': 'welcome to ragister page', 'Register': register_form}
    return render(request,'register.html',context)