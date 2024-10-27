from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 외래 키의 ForeignKey 클래스 작성 위치에 관계 없이 테이블에서는 맨 뒤쪽에 생성됨
    # 필드 명은 상대 모델 클래스명의 단수형으로 작성
    # 데이터 무결성 원칙을 지키기 위한 두 가지 방법
    #   - 게시글을 삭제했을 때 달려있는 댓글
    # .도 모두 삭제(on_delete의 CASCADE)
    #   - 댓글이 달려있는 게시글은 삭제할 수 없도록 처리
    # article = models.ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을 때 어떻게 처리할지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)