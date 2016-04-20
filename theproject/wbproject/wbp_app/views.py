from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def index(request):
	'''
	This method redirects to a users profile if they are logged in,
	otherwise, it loads the home (login) page
	'''
	if request.user.is_authenticated():
		return render(request, 'profile.html', {})
	return render(request, 'index.html', {})

def login_user(request):
	''' 
	This method authenticates the user and logs them in if they exist,
	otherwise it redirects them to the home page to login.
	'''

	if request.user.is_authenticated():
		return render(request, 'profile.html', {'user': request.user})
	elif request.method == 'POST':	
		username = request.POST['username_login']
		password = request.POST['password_login']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'profile.html', {'user': user})
			else:
				return render(request, 'index.html', {'active': False})
		else:
			return render(request, 'index.html', {'valid': False})
	return render(request, 'index.html', {})

def logout_user(request):

    logout(request)
    return render(request, 'index.html', {'loggedout': True})
