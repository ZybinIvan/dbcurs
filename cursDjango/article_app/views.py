from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import ArticleCreateForm


def render_article(request, id):
    article = get_object_or_404(Article, pk=id)
    article.views += 1
    article.save()

    is_redactor_or_admin = False
    if request.user.is_authenticated:
        is_redactor_or_admin = request.user.groups.filter(
            name='Admin').exists() or request.user == article.author

    return render(request, 'article_card.html', {'instance': article, 'is_redactor_or_admin': is_redactor_or_admin})


def render_start(request):
    articles = Article.objects.all().order_by('-created_at')

    return render(request, 'start.html', {'articles': articles})


def create_article(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        form = ArticleCreateForm()
        return render(request, 'create.html', {'form': form})

    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('profile', id=request.user.id)
        else:
            return render(request, 'create.html', {'form': form})


def delete_article(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    return redirect('start')
