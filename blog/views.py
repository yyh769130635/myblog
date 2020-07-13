from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title','TITLE')
    context = request.POST.get('context','CONTEXT')
    article_id = request.POST.get('article_id','0')
    #print(type(article_id))
    #print(article_id)
    #print(article_id=='0')
    # 对象不存在就创建

    if int(article_id) == 0 :
        print("ok")
        models.Article.objects.create(title=title, context=context)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    print("no")
    #存在在原来上面修改
    article = models.Article.objects.get(pk = article_id)
    article.title=title
    article.context = context
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})