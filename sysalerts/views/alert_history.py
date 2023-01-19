from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from sysalerts.models import *
import datetime


def alert_history(request):
    history = abnormal_condition.history.all().order_by("-date_edited")
    print(history)
    return render(request, 'alert_history.html',{'history':history})
   
