
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http import Http404
from django.http.response import Http404
from django.template import loader
from .models import Question
from django.shortcuts import render, get_object_or_404
# Create your views here.
# Client로 부터 Request 를 받아서 Response해준다


def index(request):
    # 1 return HttpResponse("Hello, World.")

    # 2 latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 3 latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 1 try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # # return HttpResponse("You're looking at question %s." % question_id)
    # return render(request, 'polls/detail.html', {'qustion': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
