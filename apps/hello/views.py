import json
from apps.hello.models import Person, Request
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    person = Person.objects.first()
    return render(request, 'contact_page.html', {'person': person})


def requests(request):
    ten_requests = Request.objects.order_by('-id')[:10]
    count = Request.objects.count()
    if request.is_ajax():
        response_data = {
            'request': [
                "Method:'{}' Path:'{}' Time:'{}'".format(
                    req.method, req.path, req.time) for req in ten_requests
                ],
            'count': count

        }
        return HttpResponse(json.dumps(response_data))
    return render(request, 'requests_page.html', {'requests': ten_requests})
