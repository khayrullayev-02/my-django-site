from django.shortcuts import render
from .models import Loyha
from news.models import News
from group.models import Group

def loyha_list(request):
    loyhalar = Loyha.objects.all()
    newslar = News.objects.all()
    groups = Group.objects.all()

    return render(request, 'loyha.html', {
        'loyhalar': loyhalar,
        'newslar': newslar,
        'groups': groups
    })
