import json
from apps.hello.models import Person, Request
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})


def requests(request):
    requests = Request.objects.order_by('-time')[:10]
    if request.is_ajax():
        response_data = {
            'request': [
                "Method:'{}' Path:'{}' Time:'{}'".format(
                    req.method, req.path, req.time) for req in requests
                ]
        }
        return HttpResponse(json.dumps(response_data))
    return render(request, 'requests_page.html', {'requests': requests})
