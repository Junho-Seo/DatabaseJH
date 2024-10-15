from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


from django.contrib.auth import get_user_model

def profile(request, username):
    # 어떤 유저의 프로필을 보여줄지 조회(username 사용하여 조회)
    # django에서는 username도 pk와 같이 식별자로 사용가능(중복 username 불가)
    # 유저 클래스는 직접 참조하지 않고 간접적으로 참조 (get_user_model 함수 사용)
    # 현재 활성화된 유저 객체 모델을 반환받아 반환값을 활용(복습)
    # get_user_model().objects.get(username=username)  # 아래 두 줄과 동일코드
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    User = get_user_model()
    # 팔로우 요청을 보내는 대상 (db에서 조회한 유저 객체)
    you = User.objects.get(pk=user_pk)
    # 나 (팔로우 요청하는 사람) (요청을 보낸 유저 객체)
    me = request.user

    # 나와 팔로우 대상자가 같지 않을 경우만 진행 (다른 사람과만 팔로우 가능)
    if me != you:
    # 만약 내가 상대방의 팔로워 목록(역참조)에 이미 있다면 팔로우 취소
        if me in you.followers.all():
            you.followers.remove(me)
            # me.followings.remove(you) # 위와 같은 코드
        else:
            you.followers.add(me)
            # me.followings.add(you) # 위와 같은 코드
    return redirect('accounts:profile', you.username)