from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from dusetteblog.apps.blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^articles/$', login_required(ArticleListView.as_view(), login_url='/'), name='article-list'),
    url(r'^article/(?P<slug>[^\.]+)/$', login_required(ArticleDetailView.as_view(), login_url='/'), name='article-detail'),
]