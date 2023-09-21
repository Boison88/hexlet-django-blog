from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleCommentsView,
    ArticleFormCreateView,
    ArticleFormView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', ArticleView.as_view(), name='articles'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
