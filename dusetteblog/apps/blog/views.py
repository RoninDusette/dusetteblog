from django.views.generic import ListView, DetailView
from dusetteblog.apps.blog.models import Article


class ArticleListView(ListView):

    model = Article
    template_name = "blog/article-list.html"


class ArticleDetailView(DetailView):

    model = Article
    template_name = "blog/article-detail.html"