from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Country,City

# Create your views here.

def index(request):
    return HttpResponse("Hello World index")

def cities(request):
    output=""
    list_cities=City.objects.all()
    for city in list_cities:
        output+=city.name+","
    return HttpResponse(output)

def countries(request):
    output2=""
    list_countries=Country.objects.all()
    for country in list_countries:
        output2+=country.name+","
    return HttpResponse(output2)

def page(request):
    # first option
    # page_loaded=loader.get_template('world/index.html')
    # return HttpResponse(page_loaded.render({},request))

    # another option
    return render(request, 'world/index.html', {})

def error(request, question_id):
    try:
        country = Country.objects.get(pk=question_id)
    except Country.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'world/404.html', {'country':country})
