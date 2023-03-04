from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

def homepage_view(request):
    context = {}
    if not len(Article.objects.all()) > 0:
        pass
        # return HttpResponse("<h4> No Articles Yet </h4>")
    
    articles = Article.objects.all().order_by("-id")
    context = {'articles':articles}    
    return render(request, 'homepage.html', context)