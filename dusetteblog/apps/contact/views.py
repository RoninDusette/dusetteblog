from django.views.generic import TemplateView
from dusetteblog.apps.blog.models import Article, Category


class ContactView(TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context


class ThanksView(TemplateView):
    template_name = "contact/thanks.html"

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['categories'] = Category.objects.all()
        return context