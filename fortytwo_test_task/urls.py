from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.hello.views.contact', name='contact_page_view'),
    url(
        r'^requests$',
        TemplateView.as_view(template_name='requests_page.html'),
        name='requests_page_view'
    ),
]
urlpatterns += staticfiles_urlpatterns()
