from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

class LoginForm(ModelForm):

	class Meta:
		moddel = User
		fields = ('username', 'password')
		widgets = {
			'password': PasswordInput(),
		}
	