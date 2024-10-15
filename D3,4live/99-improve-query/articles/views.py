from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count


# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk') # 기존 문제 코드
    articles = Article.objects.annotate(Count('comment')).order_by('-pk') # 개선 코드
    # 댓글의 개수까지 같이 포함해서 결과 출력 (SQL의 GROUP BY 활용)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)


def index_2(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
    # 작가의 이름까지 같이 포함해서 결과 출력 (SQL의 INNER JOIN 활용)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)


def index_3(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    # 역참조를 포함하여(댓글) 결과 출력 (Python의 join기능 활용)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch


def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
