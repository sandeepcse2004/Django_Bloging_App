from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from . import forms


# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_display.html', {'articles': articles})


def profile(request):
    return HttpResponse('Hello profile')


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:home')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
