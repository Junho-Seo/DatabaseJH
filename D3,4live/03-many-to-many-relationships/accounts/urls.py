from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # variable routing에서 컨버터 타입을 생략하면 기본 값은 str
    # <str:username> = <username>
    # 주의사항: 문자열을 이용한 variable routing만 이용한 url작성시
    # url 검색 순서(위에서 아래로)에 따라 해당 라인 아래로는 실행되지 않음.
    # ex) path('<username>/', views.profile, name='profile'),
    # 해당 라인 위에서 일치하지 않는 모든 주소는 해당 라인에서 문자열 변수로 받기 때문
    # (username을 검색하여 일치한다고 처리)
    # 따라서 이러한 주소는 최하단에 작성하거나 앞에 다른 문자열 주소를 섞어 작성한다.
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
