from django.shortcuts import get_object_or_404,render
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try :
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNetExit) :
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "you didn't select a choice."})
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question': question})

