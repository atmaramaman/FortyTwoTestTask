from apps.hello.models import Person, Request
from django.shortcuts import render


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})


def requests(request):
    requests = Request.objects.order_by('-time')[:10]
    return render(request, 'requests_page.html', {'requests': requests})
