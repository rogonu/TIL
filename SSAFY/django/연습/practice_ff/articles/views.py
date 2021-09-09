from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods,require_POST
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)
#new
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)

#cretae
@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title = title, content= content)
    # article.save()
    
    # return redirect('articles:detail', article.pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # else:
        #     return redirect('articles:new')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
#detail
def detail(request, pk):
    article = get_object_or_404(Article, pk = pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

#delete
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk = pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail',article.pk)

#edit
# def edit(request,pk):
#     article = Article.objects.get(pk = pk)
#     context ={
#         'article' : article
#     }
#     return render(request, 'articles/edit.html', context )
#update
@require_http_methods(['GET', 'POST'])
def update(request,pk):
    # article = Article.objects.get(pk = pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    
    article = get_object_or_404(Article, pk = pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article
    }
    return render(request, 'articles/update.html', context)
  