from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.hello.views.contact', name='contact_page_view'),
]
