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

