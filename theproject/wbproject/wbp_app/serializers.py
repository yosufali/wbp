from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ('user', 'title', 'role', 'extension_no',
		'mobile_no', 'emergency_contact', 'phd_status',
		'employable', 'max_hours', 'photo')
