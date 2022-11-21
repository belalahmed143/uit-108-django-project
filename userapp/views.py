from django.shortcuts import render,redirect

from .forms import *
from django.contrib import messages


def register(request):
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')      
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect('home')
    else:
        form =RegisterForm()
    return render(request, 'userapp/registration.html',{'form':form})
