from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is a test.")

def newsletter(request):
    return HttpResponse("newsletter placeholder")

def media(request):
    return HttpResponse("media placeholder")

def calendar(request):
    return HttpResponse("calendar placeholder")

def contact(request):
    return HttpResponse("contact placeholder")
