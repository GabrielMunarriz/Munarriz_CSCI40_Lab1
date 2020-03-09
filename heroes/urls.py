from django.conf.urls import url
from .views import HomeView, CloudView, SunfloweyView, JesterView

urlpatterns = [
	path('', views.HomeView.as_view(), name="home_view"),
	path('heroes', views.HomeView.as_view(), name="home_view"),
	path('hero/cloud/', views.CloudView.as_view(), name="cloud_view"),
	path('hero/sunflowey/', views.SunfloweyView.as_view(), name="sunflowey_view"),
	path('hero/jester/', views.JesterView.as_view(), name="jester_view"),
]