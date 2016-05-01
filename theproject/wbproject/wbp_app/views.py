from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Profile
def index(request):
	'''
	This method redirects to a users profile if they are logged in,
	otherwise, it loads the home (login) page
	'''
	if request.user.is_authenticated():
		up = Profile.objects.get(user=request.user)
		if up is not None:
			return render(request, 'profile.html', {'user': request.user, 'profile': up})
		else:
			return render(request, 'profile.html', {'user': request.user})
	return render(request, 'index.html', {})

def login_user(request):
	''' 
	This method authenticates the user and logs them in if they exist,
	otherwise it redirects them to the home page to login.
	'''

	if request.user.is_authenticated():
		up = Profile.objects.get(user=request.user)
		return render(request, 'profile.html', {'user': request.user, 'profile': up})
	elif request.method == 'POST':
		username = request.POST['username_login']
		password = request.POST['password_login']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				up = Profile.objects.get(user=request.user)
				return render(request, 'profile.html', {'user': user, 'profile': up})
			else:
				return render(request, 'index.html', {'active': False})
		else:
			return render(request, 'index.html', {'valid': False})
	return render(request, 'index.html', {})

def logout_user(request):

    logout(request)
    return render(request, 'index.html', {'loggedout': True})
