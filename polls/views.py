from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question {question}.".format(question=question_id))


def results(request, question_id):
    response = "You're looking at the results of question {question}."
    return HttpResponse(response.format(question=question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)  # aren't we supposed to be using .format in python 3?
