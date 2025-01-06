from django.shortcuts import render
from apps.models import Data


def index(request):
    posts = Data.objects.all()
    return render(request, 'home.html', {'posts': posts})