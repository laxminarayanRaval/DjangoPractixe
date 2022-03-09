from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from polls.models import Question



def index(request):
    latest_ques_list = Question.objects.order_by('-pub_date')[:5]
    # output = "<h1>"+'</h1><h1> '.join([q.que_text for q in latest_ques_list])+"</h1>"
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({'que_list': latest_ques_list}, request))

def detail(request, que_id):
    que_detail = get_object_or_404(Question, pk=que_id)
    # try:
        # que_detail = Question.objects.get(id=que_id).que_text
    # except:
        # raise Http404("Question Not Found")
    return render(request, 'polls/index.html', {'que': que_detail})
    # return HttpResponse(f"You are looking at question {que_detail}")

def results(request, que_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % que_id)

def vote(request, que_id):
    return HttpResponse("You're voting on question %s." % que_id)