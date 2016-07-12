from models import Request


class RequestsToDB(object):

    def process_request(self, request):

        method = request.META['REQUEST_METHOD']
        path = request.path
        request = Request(method=method, path=path)
        request.save()
