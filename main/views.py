from django.shortcuts import render
from django.views.generic import View
from .forms import SusForm


class Home(View):
	def get(self,request):
		template_name='main/subscripcion.html'
		form = SusForm()
		context={
		'form': form,
		}
		return render (request, template_name, context)
# Create your views here.
