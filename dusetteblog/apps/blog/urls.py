from django.conf.urls import url
from dusetteblog.apps.blog.views import ArticleListView, ArticleDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[^\.]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<slug>[^\.]+)/$', CategoryDetailView.as_view(), name='category-detail'),
]