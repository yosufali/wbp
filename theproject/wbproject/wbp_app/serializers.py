from rest_framework import serializers
from .models import Profile, Module
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	#profile = serializers.PrimaryKeyRelatedField()

	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Profile
		fields = ('user', 'title', 'role', 'extension_no',
		'mobile_no', 'emergency_contact', 'phd_status',
		'employable', 'max_hours', 'photo', 'owner')

class ModuleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Module
		fileds = ('module_code', 'name', 'leader',
			'moodle_link', 'users')