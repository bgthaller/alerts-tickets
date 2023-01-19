from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
#from sysalerts.models import abnormal_condition
import datetime

def home(request):
   
    
    return render(request, 'home.html')