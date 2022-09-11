from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
## test
def ping(request):
    return HttpResponse('Pong!', status=200)
## view all contacts

def list_all_contacts(request):
    pass

# creat contac
def create_contact(request):
    pass