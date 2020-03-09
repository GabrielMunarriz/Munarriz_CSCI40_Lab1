from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
	template_name = "home.html"
	
class CloudPageView(TemplateView):
	template_name = "detail_cloud.html"
	
class SunfloweyPageView(TemplateView):
	template_name = "detail_sunflowey.html"

class JesterPageView(TemplateView):
	template_name = "detail_jester.html"