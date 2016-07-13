from models import Request


class RequestsToDB(object):
    """ The middleware storing requests to db except page with requests """

    def process_request(self, request):

        method = request.method
        path = request.path
        if not request.is_ajax() and path != '/requests/':
            request = Request(method=method, path=path)
            request.save()
