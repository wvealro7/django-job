from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignupForm


def signup(request):
    ''' Registration'''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/dashboard/')

    else:
        form = SignupForm()

    return render(request,'registration/register.html',{'form':form})
