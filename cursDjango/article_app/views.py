from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import UserRegistrationForm, UserLoginForm


def render_article(request, id):
    test = get_object_or_404(Article, pk=id)

    return render(request, 'article_card.html', {'instance': test})


def render_start(request):
    articles = Article.objects.all()  # Получение всех статей
    return render(request, 'start.html', {'articles': articles})


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