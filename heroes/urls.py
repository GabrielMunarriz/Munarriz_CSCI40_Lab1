from django.conf.urls import url
from .views import HomeView, CloudView, SunfloweyView, JesterView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name="home"),
	url(r'heroes', HomeView.as_view(), name="home"),
	url(r'hero/cloud/', CloudView.as_view(), name="detail_cloud"),
	url(r'hero/sunflowey/', SunfloweyView.as_view(), name="detail_sunflowey"),
	url(r'hero/jester/', JesterView.as_view(), name="detail_jester"),
]