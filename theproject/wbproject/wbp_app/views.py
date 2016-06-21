from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Module, Lecture

def index(request):
	'''
	This method redirects to a users profile if they are logged in,
	otherwise, it loads the home (login) page
	'''
	if request.user.is_authenticated():
		user_profile = Profile.objects.get(user=request.user)
		modules = Module.objects.filter(users=request.user)

		lectures = []
		tutorials = []
		for m in modules:
			lectures.extend(list(Lecture.objects.filter(module=m)))
			tutorials.extend(list(Tutorial.objects.filter(module=m)))

		return render(request, 'profile.html', {'user': request.user, 'profile': user_profile, 'modules': modules, 'lectures': lectures, 'tutorials': tutorials})
	return render(request, 'index.html', {})


def show_modules(request):
	'''
	This method is used to load up the /modules/ page.
	'''
	if request.user.is_authenticated():
		user_profile = Profile.objects.get(user=request.user)
		modules = Module.objects.filter(users=request.user)

		return render(request, 'myModules.html', {'user': request.user, 'profile': user_profile, 'modules': modules})
	return render(request, 'index.html', {})


def login_user(request):
	''' 
	This method authenticates the user and logs them in if they exist,
	otherwise it redirects them to the home page to login.
	'''

	if request.user.is_authenticated():
		user_profile = Profile.objects.get(user=request.user)
		modules = Module.objects.filter(users=request.user)
		return render(request, 'profile.html', {'user': request.user, 'profile': user_profile, 'modules': modules})
	elif request.method == 'POST':
		username = request.POST['username_login']
		password = request.POST['password_login']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				user_profile = Profile.objects.get(user=request.user)
				modules = Module.objects.filter(users=request.user)
				return render(request, 'profile.html', {'user': user, 'profile': user_profile, 'modules': modules})
			else:
				return render(request, 'index.html', {'active': False})
		else:
			return render(request, 'index.html', {'valid': False})
	return render(request, 'index.html', {})

def logout_user(request):

    logout(request)
    return render(request, 'index.html', {'loggedout': True})

from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse

def reset(request):

	return password_reset(request, post_reset_redirect=reverse('index'))

def reset_confirm(request, uidb64=None, token=None):

	return password_reset_confirm(request, uidb64=uidb36, token=token, post_reset_redirect=reverse('index'))

# ----------------------------------------------
# API Stuff

from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Profile, Module, Lecture, Tutorial
from .serializers import ProfileSerializer, UserSerializer, ModuleSerializer, LectureSerializer, TutorialSerializer
from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# Profile Views

class ProfileList(APIView):
    """
    List all Profiles, or create a new profile.
    """

    def get(self, request, format=None):
    	profiles = Profile.objects.all()
    	serializer = ProfileSerializer(profiles, many=True)
    	return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = ProfileSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

class ProfileDetail(APIView):
    """
    Retrieve, update or delete a profile.
    """

    def get_object(self, user_id):
    	try:
    		return Profile.objects.get(user_id=user_id)
    	except Profile.DoesNotExist:
    		raise Http404

    def get(self, request, user_id, format=None):
    	profile = self.get_object(user_id)
    	serializer = ProfileSerializer(profile)
    	return Response(serializer.data)

    def put(self, request, user_id, format=None):
    	profile = self.get_object(user_id)
    	serializer = ProfileSerializer(profile, data=request.data)
    	if serializer.is_valid:
    		serializer.save()
    		return Response(serializer.data)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
    	profile = self.get_object(user_id)
    	profile.delete()
    	return Response(status=status.HTTP_204_NO_CONTENT)

# User Views

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# Module Views

class ModuleList(generics.ListAPIView):
	queryset = Module.objects.all()
	serializer_class = ModuleSerializer

class ModuleDetail(generics.RetrieveAPIView):
	queryset = Module.objects.all()
	serializer_class = ModuleSerializer

# Lecture Views

class LectureList(generics.ListAPIView):
	queryset = Lecture.objects.all()
	serializer_class = LectureSerializer

class LectureDetail(generics.RetrieveAPIView):
	queryset = Lecture.objects.all()
	serializer_class = LectureSerializer

# Tutorial Views

class TutorialList(generics.ListAPIView):
	queryset = Tutorial.objects.all()
	serializer_class = TutorialSerializer

class TutorialDetail(generics.RetrieveAPIView):
	queryset = Tutorial.objects.all()
	serializer_class = TutorialSerializer