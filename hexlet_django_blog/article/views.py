from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class IndexView(TemplateView):

    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))
