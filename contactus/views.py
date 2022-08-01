from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from  django.contrib.auth.decorators import login_required



@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,message="request sent sucecssfully...")

            redirect('contact')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
