from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, 'articles/articles_display.html')
            return redirect('articles:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})
