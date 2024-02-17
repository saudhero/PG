from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
       path('phishing-detection/', views.phishing_detection, name='phishing-detection'),
    path('articles/', views.articles, name='articles'),
    path('video/', views.video, name='video'),
    
]