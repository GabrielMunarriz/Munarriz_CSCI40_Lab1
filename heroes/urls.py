from django.conf.urls import url
from .views import HomePageView, CloudPageView, SunfloweyPageView, JesterPageView

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name="home"),
	url(r'heroes', HomePageView.as_view(), name="home"),
	url(r'hero/cloud/', CloudPageView.as_view(), name="detail_cloud"),
	url(r'hero/sunflowey/', SunfloweyPageView.as_view(), name="detail_sunflowey"),
	url(r'hero/jester/', JesterPageView.as_view(), name="detail_jester"),
]