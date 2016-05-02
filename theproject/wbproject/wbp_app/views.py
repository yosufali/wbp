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
