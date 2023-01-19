from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from sysalerts.forms import abnormal_cond_form
from sysalerts.models import abnormal_condition
import datetime

def edit_alert(request, id=0):
    if request.method == "GET":
            alertupdate= abnormal_condition.objects.get(pk=id)
            form = abnormal_cond_form(instance=alertupdate)
            return render(request, 'edit_alert.html', {'form':form})
    else:
      
       
        alertupdate= abnormal_condition.objects.get(pk=id)
        form = abnormal_cond_form(request.POST, instance = alertupdate)
        if form.is_valid():
            settime=form.save(commit=False)                       
            settime.date_edited = (datetime.datetime.now())
            settime.user_name = str(request.user)
            settime.save()
        else:
            print('did not save')
            print(form.errors)

        return redirect(reverse_lazy('sysalerts:alert_list'))


def alt_complete(request,id):
    selected_condition = abnormal_condition.objects.get(pk=id)
    selected_condition.complete= True   
    selected_condition.date_edited = (datetime.datetime.now())
    selected_condition.user_name = str(request.user)
    selected_condition.date_completed = (datetime.datetime.now())
    
    selected_condition.save()
    return redirect(reverse_lazy('sysalerts:alert_list'))
