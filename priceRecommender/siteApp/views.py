from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import validators

from .models import AirbnbRequest, Amenities
from .forms import AirbnbRequestForm
import xgboostPrediction as ap
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AirbnbRequestForm(request.POST)
        if form.is_valid():
            price = ap.SiteappPythonBack.getPrediction(form)
            return HttpResponse("GoodJobBoy you price is!",price,"yay!")
        else:
            raise ValidationError('Invalid value', code='invalid')
    else:
        form = AirbnbRequestForm()
        return render(request, 'siteApp/index.html', {'form': form})

#def processForm(request):





# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        