from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):
    return HttpResponse("Hi this is Sachin, this will also pass")
