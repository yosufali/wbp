from rest_framework import serializers
from .models import Profile, Module, Lecture, Tutorial
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	'''
	The Serialier for the User model, helps with turning a User object into JSON
	and back again
	'''
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
	'''
	The Serialier for the Profile model, helps with turning a Profile object into JSON
	and back again
	'''
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Profile
		fields = ('user', 'title', 'role', 'extension_no',
		'mobile_no', 'emergency_contact', 'phd_status',
		'employable', 'max_hours', 'photo', 'owner')

class ModuleSerializer(serializers.ModelSerializer):
	'''
	The Serialier for the Module model, helps with turning a Module object into JSON
	and back again
	'''
	class Meta:
		model = Module
		fileds = ('module_code', 'name', 'leader',
			'moodle_link', 'users')

class LectureSerializer(serializers.ModelSerializer):
	'''
	The Serialier for the Lecture model, helps with turning a Lecture object into JSON
	and back again
	'''
	class Meta:
		model = Lecture
        fields = ('id','lecture_date', 'lecture_start_time',
			'lecture_end_time', 'lecture_location',
			'module')

class TutorialSerializer(serializers.ModelSerializer):
    '''
    The Serialier for the Tutorial model, helps with turning a Tutorial object into JSON
    and back again
    '''
    class Meta:
        model = Tutorial
        fields = ("id","tutorial_date", "tutorial_start_time", 
			"tutorial_end_time", "tutorial_group",
			"tutorial_location", "module", "users")
