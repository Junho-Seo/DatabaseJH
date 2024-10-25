from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# 문제 1
'''
 ❖ Request : GET /api/v1/article_list/
 ❖작성된모든Article 목록을요청했을때, id, title 필드정보만응답으로나타낼수있도록
ArticleListSerializer를작성하시오.
 ❖수정파일:articles/serializers.py
'''

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title')