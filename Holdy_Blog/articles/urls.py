
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.article_create, name='create'),
    path('<slug>/', views.article_detail, name='detail'),
]
