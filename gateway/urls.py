from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^summary/(?P<merchant_id>[0-9]+)/$', views.summary, name='summary'),
    url(r'^$', views.transaction, name='manage'),
    url(r'^admin', admin.site.urls),
]
