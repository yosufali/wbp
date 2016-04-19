from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	''' This method simply loads the home page where users can login to the system. '''
	# TODO: If they'relogged in already, redirect to thier profile page.
	return render(request, 'index.html', {})

def login_user(request):
	''' The method authenticates the user and logs them in if they exist. '''

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