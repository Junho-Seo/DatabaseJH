from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 다대다 필드이기 때문에 변수명 복수형 권장(followings, followers)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # - 우리가 만드는 기능에서는 대칭이 켜져있으면 안된다(팔로잉,팔로우 기능)
    # - 역참조명 설정 필요한 이유: user_set 은 해당 기능의 역참조가 무슨 역할을 하는지 알기 어렵다(가독성)
    # ex) user1을 팔로우하는 사람들 조회: user1.followers.all() = user1.user_set.all()
    # - 나를 중심으로 생각했을 때 다른 사람을 참조할 때(정참조, 변수명, followings)
    # - 다른 유저가 나를 참조 할 때(역참조, followers)
    # - 물론 재귀적 다대다 관계이기 때문에 두 키워드가 바뀌어도 작동되지만,
    #   본 예제에서는 사람이 생각했을 때 편한 방향으로 설정함.
