from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegistrationForm, UserLoginForm
from article_app.models import Article


def sign_up_form(request):
    if request.user.is_authenticated:
        return redirect('start')

    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('start')
        else:
            return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Пользователь успешно вошел
                return redirect('start')
            else:
                # Неверные учетные данные
                messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def render_user(request, id):
    usr = get_object_or_404(User, pk=id)
    articles = Article.objects.filter(author=usr).order_by('-created_at')
    is_own_profile = request.user.id == id

    is_redactor_or_admin = usr.groups.filter(name='Redactor').exists() or usr.groups.filter(name='Admin').exists()

    return render(request, 'profile.html', {'user': usr, 'articles': articles, 'is_own_profile': is_own_profile,
                                            'is_redactor_or_admin': is_redactor_or_admin})
