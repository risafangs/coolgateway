from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='hello.html'), name='index'),
    url(r'^gateway/', include('gateway.urls')),
    url(r'^admin/', admin.site.urls),
]
