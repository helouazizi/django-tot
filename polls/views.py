from django.http import HttpResponse
from django.template import loader
from .models import  Question

# Create your views here.


def index(req):
    latest_Questions = Question.objects.all().order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    # lets clear the output
    context = {'latest_Questions': latest_Questions}
    # output = ", ".join([q.question_text for q in latest_Questions])
    return HttpResponse(template.render(context,req))



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)