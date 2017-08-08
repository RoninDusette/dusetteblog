from django.views.generic import ListView, DetailView
from dusetteblog.apps.blog.models import Article, Category


class ArticleListView(ListView):

    model = Article
    template_name = "blog/article-list.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):

    model = Article
    template_name = "blog/article-detail.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CategoryListView(ListView):

    model = Category
    template_name = "blog/category-list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CategoryDetailView(ListView):

    model = Article
    template_name = "blog/category-detail.html"

    def get_queryset(self):
        current_category = self.kwargs['slug']
        return Article.objects.filter(category__slug=current_category)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        context['category_name'] = self.kwargs['slug']
        return context
