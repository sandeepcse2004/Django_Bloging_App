from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_display.html', {'articles' : articles})

def profile(request):
    return HttpResponse('Hello profile')

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article' : article})
