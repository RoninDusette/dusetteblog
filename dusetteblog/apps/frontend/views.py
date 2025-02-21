from django.views.generic import TemplateView
from dusetteblog.apps.blog.models import Article, Category
from dusetteblog.apps.item_shop_specials.models import ItemShopSpecials


class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        context['specials'] = ItemShopSpecials.objects.all()
        return context
