from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Module
def index(request):
	'''
	This method redirects to a users profile if they are logged in,
	otherwise, it loads the home (login) page
	'''
	if request.user.is_authenticated():
		user_profile = Profile.objects.get(user=request.user)
		modules = Module.objects.filter(users=request.user)

		if up is not None:
			return render(request, 'profile.html', {'user': request.user, 'profile': user_profile, 'modules': modules})
		else:
			return render(request, 'profile.html', {'user': request.user})
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

# ----------------------------------------------
# API Stuff

from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


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
