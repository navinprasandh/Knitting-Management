from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

def home(request):
	return render(request,'homepage.html')

class reg(SuccessMessageMixin, CreateView):
	success_url = reverse_lazy('home')
	success_message = 'Machine entry has been sucessfully updated!'
	form_class = Machine
	template_name = 'forms.html'

def wstatus(request):
	return render(request,'status.html')