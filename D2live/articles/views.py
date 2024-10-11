from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm
    # 해당 게시글에 작성된 모든 댓글 조회 (역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    # request 확인하는법
    # 아래 코드처럼 맨 위에 print(request) 찍어보면 된다.
    # print(request)  # <WSGIRequest: POST '/articles/create/'>
    # print(request.user)  # admin (요청 유저 이름)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # print(request.user, article.user)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


def comments_create(request, pk):
    # 이 함수로 GET 요청을 보내는 경우가 없기 때문에 아래 구조는 사용하지 않음
    # detail 페이지를 사용하기 때문에 get이 오는 경우를 고려할 필요도 없음
    # if request.method == "POST":
    #     pass
    # else:
    #     pass
    
    # 어떤 게시글에 작성되는지 게시글을 조회
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # save 전에 외래 키 데이터를 넣는 타이밍이 필요
        # 외래 키를 넣기 위한 2가지 조건
        #   1. comment 인스턴스 필요
        #   2. save 메서드가 호출되기 전이어야 함
        #   문제상황: comment 인스턴스는 save메서드가 호출되어야 생성됨
        #       그래서 django의 save 메서드는 인스턴스만 제공하고, 
        #       실제 저장은 잠시 대기하는 옵션을 제공한다.
        comment = comment_form.save(commit=False) # 기본 값: commit = True
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글을 삭제할지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # detail에 article_pk를 넘기는 첫 번째 방법
    # article_pk = comment.article.pk
    # 두 번째 방법 (url 구성을 일치시킬 수 있는 이 방법을 선호)
    article = Article.objects.get(pk=article_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article.pk)