from django import forms
from .models import Questboard

# class KeyForm(forms.ModelForm):
# 	class Meta:
# 		model = Key
# 		fields = ['name', 'description'] 

class CreateQuestboardForm(forms.ModelForm):
	class Meta:
		model = Questboard
		fields = ['name', 'description', 'required_stars']
		widgets = {
			'description': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
		}