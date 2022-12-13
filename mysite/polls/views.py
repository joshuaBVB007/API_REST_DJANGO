from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Question,Choice
from django.template import loader


# Create your views here.
def index(request):
    # latest_question_list = Choice.objects.order_by('-id')[:5]
    # output = ', '.join([q.choice_text for q in latest_question_list])
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #with render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return render(request, 'index.html', {} )

# As you can see every method represents a view that contains and httpresponse