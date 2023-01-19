from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from sysalerts.models import abnormal_condition,ticket
import datetime


def view_tickets(request):
    tks = ticket.objects.all().order_by("-date_created")
   
    return render(request, 'tickets_view.html',{'tks':tks})
   
