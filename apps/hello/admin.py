from django.contrib import admin

from apps.hello.models import Person, Request

admin.site.register(Person)
admin.site.register(Request)
