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
			'name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
			'description': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
			'required_stars': forms.Textarea(attrs={'cols': 4, 'rows': 1}),
		}