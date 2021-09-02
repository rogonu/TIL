from django.shortcuts import render, redirect #, redirect 둘중에 하나만 
from .models import Article #명시적 상대 경로
# Create your views here.
def index(request):
    #작성한 모든 게시글을 출력
    # 1. 모든 게시글 조회
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    #new 로부터 title과 content 를 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 2 번째 방법  앞으로 이방법 쓸거임 저장전에 유효성 검사를 위해서임
    article = Article(title=title, content = content)
    article.save()
    # 3번째 방법
    # Article.objects.create(title = title, content=content)
    return redirect('articles:detail', article.pk)
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context ={
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    pass
