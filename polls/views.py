from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Greetings humans! You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question {question}.".format(question=question_id))


def results(request, question_id):
    response = "You're looking at the results of question {question}."
    return HttpResponse(response.format(question=question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)  # aren't we supposed to be using .format in python 3?
