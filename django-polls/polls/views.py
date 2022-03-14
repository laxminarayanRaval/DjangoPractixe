from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic  # for making generic views
from django.utils import timezone  # for view tests 
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_ques_list'

    def get_queryset(self):
        """Return the last five published Questions. (not including those set be published in future)."""
        return [que for que in Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date') if que.choice_set.all()][:5]  # first filter Que. by Decs Pub_date then check Choice then splice top 5
        # ).order_by('-pub_date')[:5] if que.choice_set.all()]  # first filter top 5 Que. by Decs Pub_date then check Choice 

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

"""
def index(request):
    latest_ques_list = Question.objects.order_by('-pub_date')[:5]
    # output = "<h1>"+'</h1><h1> '.join([q.que_text for q in latest_ques_list])+"</h1>"
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({'latest_ques_list': latest_ques_list}, request))

def detail(request, que_id):
    que_detail = get_object_or_404(Question, pk=que_id)
    # try:
        # que_detail = Question.objects.get(id=que_id).que_text
    # except:
        # raise Http404("Question Not Found")
    return render(request, 'polls/details.html', {'que': que_detail})
    # return HttpResponse(f"You are looking at question {que_detail}")

def results(request, que_id):
    que_detail = get_object_or_404(Question, pk=que_id)
    data = {
        'que_id': que_id, 
        'que_text': que_detail.que_text, 
        'choices':[choice for choice in que_detail.choice_set.all()],
        'total_votes': sum([choice.vote for choice in que_detail.choice_set.all()])
        }
    # print(data)
    # response = "You're looking at the result of question %s."
    # return HttpResponse(response % que_id)
    return render(request, 'polls/result.html', {'data': data})
"""

def vote(request, que_id):
    que_detail = get_object_or_404(Question, pk=que_id)
    try:
        selected_choice = que_detail.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'que': que_detail, 'error_msg': 'Select Proper Choice.'})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(que_detail.id,)))
    # return HttpResponse("You're voting on question %s." % que_id) 
