from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    '''
    Shows the Profile fields in the default Django administration
    '''
    list_display = ["user", "title", "role", "extension_no", "mobile_no",
                "emergency_contact", "phd_status", "employable", "max_hours"]

# Actually registers the above list wit the Django admin
admin.site.register(Profile, ProfileAdmin)
