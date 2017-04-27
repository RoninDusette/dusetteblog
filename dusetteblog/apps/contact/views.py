from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "contact/contact.html"


class ThanksView(TemplateView):
    template_name = "contact/thanks.html"