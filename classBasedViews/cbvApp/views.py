from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class GreetingView(View):
    greetingMessage="<b>First CBV says hi 🙌</b>"
    def get(self,request):
        return HttpResponse(self.greetingMessage)
