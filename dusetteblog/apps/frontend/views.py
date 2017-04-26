from django.views.generic import TemplateView
from dusetteblog.apps.blog.models import Article


class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
