from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import (
    ArticleSerializer,
    ArticleListSerializer
)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        '''
        ❖ Request : POST /api/v1/article_list/ 
        ❖ ArticleSerializer를이용하여새로운Article을생성할수있도록코드를완성하시오. 
        (201 status code 도같이응답)
        ❖수정파일:articles/views.py
        '''
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        '''
        ❖ Request : PUT /api/v1/articles/<int:article_pk>/ 
        ❖ Article 정보가수정될수있도록코드를완성하시오.
        ❖수정파일:articles/views.py
        '''
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        '''
        ❖ Request : DELETE /api/v1/articles/<int:article_pk>/
        ❖작성된Article 정보가삭제될수있도록코드를완성하시오.
        ❖삭제후아래정보가응답으로전달될수있도록하시오.
        (삭제된파일의정보: {‘msg’: ‘1번파일삭제’}, 응답코드: 204)
        ❖수정파일:articles/views.py
        '''
        article.delete()
        msg = {
            'msg': f'{article_pk}번 파일 삭제',
        }
        return Response(msg, status=status.HTTP_204_NO_CONTENT)