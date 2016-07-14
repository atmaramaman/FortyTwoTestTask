from datetime import datetime
from models import Request


class RequestsToDB(object):
    """ The middleware storing requests to db except page with requests """

    def process_request(self, request):

        method = request.method
        path = request.path
        time = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
        if not request.is_ajax() and path != '/requests/':
            request = Request(method=method, path=path, time=time)
            request.save()
