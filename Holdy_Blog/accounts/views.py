from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, 'articles/articles_display.html')
            return redirect('accounts:login')
            # form1 = AuthenticationForm()
            # return render(request, 'accounts/login.html', {'form1' : form1})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(data=request.POST)
        if form1.is_valid():
            user =  form1.get_user()
            login(request,user)
            return redirect('articles:create')
    else:
        form1 = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form1' : form1})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:home')
