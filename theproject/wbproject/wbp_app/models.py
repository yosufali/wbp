from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    Custom profile thats linked to the default USer class which
    allows me to extend it and have extra fields for each user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    extension_no = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=11, null=True, blank=True)
    emergency_contact = models.CharField(max_length=11, null=True, blank=True)
    phd_status = models.BooleanField(default=False)
    employable = models.BooleanField(default=True)
    max_hours = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __unicode__(self):
    	return self.user.username

class Module(models.Model):
	'''
	Modules class that stores information related to a particular module
	'''
	module_code = models.CharField(max_length=10, unique=True)
	name = models.CharField(max_length=30)
	leader = models.CharField(max_length=30)
	moodle_link = models.URLField(max_length=200)
	users = models.ManyToManyField(User)

	def __unicode__(self):
		return self.name

class Lecture(models.Model):
    '''
    Lecture class that stores information about a particular lecture
    for a particular module
    '''
    lecture_date = models.DateField()
    lecture_start_time = models.TimeField()
    lecture_end_time = models.TimeField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __unicode__(self):
    	return "%s %s %s" % (self.module.name, self.lecture_date, self.lecture_start_time)
