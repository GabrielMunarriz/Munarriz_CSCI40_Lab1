from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.

class home_view(TemplateView):
	template_name = home.html
	
class cloud_view(TemplateView):
	template_name = detail_cloud.html
	
class sunflowey_view(TemplateView):
	template_name = detail_sunflowey.html

class jester_view(TemplateView):
	template_name = detail_jester.html