from django import forms

from .models import Article


class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Article
        fields = ['title', 'text']
