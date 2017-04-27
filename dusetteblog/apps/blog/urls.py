from django.conf.urls import url
from dusetteblog.apps.blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[^\.]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]