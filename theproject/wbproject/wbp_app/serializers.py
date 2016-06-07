from rest_framework import serializers
from .models import Profile, Module, Lecture, Tutorial
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

class LectureSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lecture
        fields = ('id','lecture_date', 'lecture_start_time',
			'lecture_end_time', 'lecture_location',
			'module')

class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ("id","tutorial_date", "tutorial_start_time", 
			"tutorial_end_time", "tutorial_group",
			"tutorial_location", "module", "users")
