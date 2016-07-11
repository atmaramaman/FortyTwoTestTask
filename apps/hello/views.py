from apps.hello.models import Person
from django.shortcuts import render


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})


def requests(request):
    context = {'method': "'GET'", 'path': "'/'", 'time': "'1989-12-22'"}
    return render(request, 'requests_page.html', context)
