from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, index Jonathan")
def view(request,id):
    return HttpResponse("Hello, View Jonathan")
def surname(request,id):
    return HttpResponse("Hello, Calderon")