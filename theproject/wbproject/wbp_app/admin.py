from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ["user", "title", "role", "extension_no", "mobile_no",
				"emergency_contact", "phd_status", "employable", "max_hours"]

#admin.site.register(Profile)
admin.site.register(Profile, ProfileAdmin)