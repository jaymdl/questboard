from django import forms
from .models import Questboard, Quest


class CreateQuestboardForm(forms.ModelForm):
	class Meta:
		model = Questboard
		fields = ['name', 'description', 'required_stars']
		widgets = {
			'name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
			'description': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
			'required_stars': forms.Textarea(attrs={'cols': 4, 'rows': 1}),
		}

class CreateQuestForm(forms.ModelForm):
	class Meta:
		model = Quest
		fields = ['name', 'description', 'stars', 'for_everyone']
		widgets = {
			'name': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
			'description': forms.Textarea(attrs={'cols': 30, 'rows': 4}),
			'stars': forms.Textarea(attrs={'cols': 4, 'rows': 1}),
		}


class MemberOneForm(forms.ModelForm):
	class Meta:
		model = Quest
		fields = ['member_one']
		

class MemberTwoForm(forms.ModelForm):
	class Meta:
		model = Quest
		fields = ['member_two']
		

class MemberThreeForm(forms.ModelForm):
	class Meta:
		model = Quest
		fields = ['member_three']
		