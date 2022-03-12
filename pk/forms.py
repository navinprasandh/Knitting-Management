from .models import *
from django import forms

class Machine(forms.ModelForm):
	class Meta:
		model=work
		fields="__all__"
		widgets={'date':forms.DateTimeInput(attrs={'type':'date'})}