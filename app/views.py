
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Questions, Choice


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_data')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'app/detail.html'
    context_object_name = "question"


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'app/results.html'
    context_object_name = "question"


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app:results', args=(question.id,)))












