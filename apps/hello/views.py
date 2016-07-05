from apps.hello.models import Person
from django.shortcuts import render


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})
