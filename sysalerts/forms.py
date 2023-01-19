from django import forms
from .models import ticket,abnormal_condition





class ticket_form(forms.ModelForm):
	class Meta:
		model = ticket
		fields = ('location','description', )
		labels = {
			'location':'Location',
			'description':'Description'			

		}

class abnormal_cond_form(forms.ModelForm):
	class Meta:
		model = abnormal_condition
		fields = ('Sub', 'feeder','location','description')
		labels = {
			'Sub':'Sub Station',
			'feeder':'Feeder',
            'location':'Location',			
            'description':'Description'			

		}
        
