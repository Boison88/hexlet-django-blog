from django import forms
from django.forms import ModelForm


class CommentArticleForm(forms.Form):
    content = forms.Charfield(label='Comment')


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']