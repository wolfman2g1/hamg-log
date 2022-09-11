from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
## test
def ping(request):
    return HttpResponse('Pong!', status=200)
