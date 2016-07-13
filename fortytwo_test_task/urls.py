from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        'apps.hello.views.contact', name='contact_page_view'),
    url(r'^requests/$',
        'apps.hello.views.requests', name='requests_page_view'),
]
urlpatterns += staticfiles_urlpatterns()
