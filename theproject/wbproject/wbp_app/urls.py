from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.login_user, name="login"),
	url(r'^logout/$', views.logout_user, name="logout"),

	url(r'^api/profiles/$', views.ProfileList.as_view()),
	url(r'^api/profiles/(?P<user_id>[0-9]+)/$', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
