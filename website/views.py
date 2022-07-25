from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request,"website/welcome.html",
    {"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("The time now is " + str(datetime.now()))

def hours(request):
    return HttpResponse("In a year there are 8760 hours")





