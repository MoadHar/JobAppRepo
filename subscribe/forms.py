from django import forms 
from django.utils.translation import gettext_lazy as _ 

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
	class Meta:
		model=Subscribe
		# fields=['firstname', 'lastname', 'email']
		fields='__all__'
		#exclude=['field_name']
		labels={
		'first_name':_('Enter first name'),
		'last_name':_('Enter last name'),
		'email':_('Enter email')
		}

		help_texts={'first_name':_('Enter characters only')}
		
		error_messages={
		'first_name':{'required':_('you cannot without first name ok')}
		}

# def validate_comma(value):
# 	if ',' in value:
# 		raise forms.ValidationError("invalidd value: plz remove the ','")

# class SubscribeForm(forms.Form):
	# first_name = forms.CharField(max_length=100, validators=[validate_comma])
	# last_name = forms.CharField(max_length=100, validators=[validate_comma])
	# email = forms.EmailField(max_length=100)

	# def clean_first_name(self):
	# 	data = self.cleaned_data["first_name"]
	# 	if ',' in data:
	# 		raise forms.ValidationError("invalid firstname, should in be no comma")

