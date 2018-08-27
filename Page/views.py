from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
def index(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>not found</h1>')
    else:
        return HttpResponse('<h1>welcome </h1>')
@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')