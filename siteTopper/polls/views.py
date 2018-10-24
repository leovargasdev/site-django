from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question


def index(request):
    questoes = Question.objects.order_by('-pub_date')[:2]
    context = {'latest_question_list': questoes}
    template = 'polls/index.html'
    return render(request, template, context)

def detail(request, question_id):
    return HttpResponse("Veja a minha questão %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
