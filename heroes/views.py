from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
	template_name = "home.html"
	
class CloudView(TemplateView):
	template_name = "detail_cloud.html"
	
class SunfloweyView(TemplateView):
	template_name = "detail_sunflowey.html"

class JesterView(TemplateView):
	template_name = "detail_jester.html"