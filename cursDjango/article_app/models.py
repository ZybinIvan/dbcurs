from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    views = models.PositiveIntegerField(verbose_name="Просмотры", default=0, null=False)

    text = models.TextField(verbose_name="Текст статьи", null=True, blank=True)

    title = models.CharField(verbose_name="Заголовок", max_length=256, null=False, blank=True)

    created_at = models.DateTimeField(verbose_name="Создан", auto_now=True)

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
