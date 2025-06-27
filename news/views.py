from django.shortcuts import render
from .models import News

def news_list(request):
    newslar = News.objects.all()
    return render(request, 'loyha.html', {'newslar': newslar})
