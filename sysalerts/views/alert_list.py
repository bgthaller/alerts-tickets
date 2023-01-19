from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from sysalerts.forms import abnormal_cond_form,ticket_form
from sysalerts.models import abnormal_condition,ticket
import datetime

# Create your views here.
def alert_list(request):
    if request.method == 'GET':

        alert_items = abnormal_condition.objects.filter(complete=False).order_by('-date_edited')
        ab_cond_form = abnormal_cond_form
        tkt_form = ticket_form
        ticket_num = len(ticket.objects.all())
       
       
    
        
        context = {'alert_items':alert_items, 'ab_cond_form':ab_cond_form,'tkt_form':tkt_form,'ticket_num':ticket_num}
        return render(request, 'alerts_list.html',context)

    else:
          # if a new alert
        value=request.POST.get('formtype') 
         
        if value == "altfield":
            
            form = abnormal_cond_form(request.POST)                                         
            
            if form.is_valid():
                print('saved')
                settime=form.save(commit=False)           
                settime.date_created = (datetime.datetime.now())
                settime.date_edited = (datetime.datetime.now())                
                settime.save()
                
            
            else:
                print('did not save')
                print(form.errors)



        else:
            form = ticket_form(request.POST)   
            if form.is_valid():
                print('saved')
                settime=form.save(commit=False)           
                settime.date_created = (datetime.datetime.now())                               
                settime.save()
            else:
                print('did not save')
                print(form.errors)
                  
           
        

    alert_items = abnormal_condition.objects.order_by('Sub')
    ab_cond_form = abnormal_cond_form
    tkt_form = ticket_form
    tks = len(ticket.objects.all().order_by("-date_created"))
    print(tks)
    
        
    context = {'alert_items':alert_items, 'ab_cond_form':ab_cond_form,'tkt_form':tkt_form}
    return redirect(reverse_lazy('sysalerts:alert_list'),context)
             
           

