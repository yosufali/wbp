from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^modules/$', views.show_modules, name='modules'),
	url(r'^settings/$', views.show_settings, name='settings'),

	url(r'^login/$', views.login_user, name="login"),
	url(r'^logout/$', views.logout_user, name="logout"),

	url(r'^reset/$', views.reset, name="reset"),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_confirm, name='password_reset_confirm'),


	url(r'^api/profiles/$', views.ProfileList.as_view()),
	url(r'^api/profiles/(?P<user_id>[0-9]+)/$', views.ProfileDetail.as_view()),

	url(r'^api/users/$', views.UserList.as_view()),
	url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

	url(r'^api/modules/$', views.ModuleList.as_view()),
	url(r'^api/modules/(?P<pk>[0-9]+)/$', views.ModuleDetail.as_view()),

	url(r'^api/lectures/$', views.LectureList.as_view()),
	url(r'^api/lectures/(?P<pk>[0-9]+)/$', views.LectureDetail.as_view()),

	url(r'^api/tutorials/$', views.TutorialList.as_view()),
	url(r'^api/tutorials/(?P<pk>[0-9]+)/$', views.TutorialDetail.as_view()),

	url(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Lets me log into the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
