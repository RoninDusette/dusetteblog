from django.conf.urls import url
from dusetteblog.apps.contact.views import ContactView, ThanksView

urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
]