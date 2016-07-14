import json
from apps.hello.models import Person, Request
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})


def requests(request):
    ten_requests = Request.objects.order_by('-id')[:10]
    new_request = Request.objects.last()
    if request.is_ajax():
        response_data = {
            'request': "Method:'{}' Path:'{}' Time:'{}'".format(
                new_request.method, new_request.path, new_request.time
                )
        }
        return HttpResponse(json.dumps(response_data))
    return render(request, 'requests_page.html', {'requests': ten_requests})
