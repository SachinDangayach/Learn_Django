from django.http import HttpResponse

class MiddleWareLifeCycle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('Before the view is executed')
        response= self.get_response(request)
        print('After the view is executed')
        return response

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response= self.get_response(request)
        return response

    def process_exception(self, request, exception):
        return HttpResponse("<b>We are currently facing some issues. Please check back in a few minutes</b>")
