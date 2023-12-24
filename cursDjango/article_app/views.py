from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Article


def func_super_puper(request, id):
    test = get_object_or_404(Article, pk=id)

    return render(request, 'detail.html', {'instance': test})
