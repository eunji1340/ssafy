from django.shortcuts import render, redirect
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 단일 게시글의 상세 페이지를 응답
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장 요청
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2.
    article = Article(title=title, content=content)
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(reqeust, pk):
    article = Article.objects.get(pk=pk)
    article.title = reqeust.POST.get('title')
    article.content = reqeust.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)