from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.login_user, name="login"),
	url(r'^logout/$', views.logout_user, name="logout"),

	url(r'^api/profiles/$', views.ProfileList.as_view()),
	url(r'^api/profiles/(?P<user_id>[0-9]+)/$', views.ProfileDetail.as_view()),

	url(r'^api/users/$', views.UserList.as_view()),
	url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

	url(r'^api/modules/$', views.ModuleList.as_view()),
	url(r'^api/modules/(?P<pk>[0-9]+)/$', views.ModuleDetail.as_view()),

	url(r'^api/lectures/$', views.LectureList.as_view()),
	url(r'^api/lectures/(?P<pk>[0-9]+)/$', views.LectureDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Lets me log into the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

