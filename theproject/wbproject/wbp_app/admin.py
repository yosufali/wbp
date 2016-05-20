from django.contrib import admin
from .models import Profile, Module, Lecture, Tutorial

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    '''
    Shows the Profile fields in the default Django administration
    '''
    list_display = ["user", "title", "role", "extension_no", "mobile_no",
                "emergency_contact", "phd_status", "employable", "max_hours"]


class ModuleAdmin(admin.ModelAdmin):
	'''
	Shows the Module fields in the default Django admin
	'''
	list_display = ["module_code", "name", "leader","moodle_link"]


class LectureAdmin(admin.ModelAdmin):
	'''
	Shows the Lecture fileds in the default Django admin
	'''
	list_display = ["lecture_date", "lecture_start_time", "lecture_end_time", "lecture_location"] 

class TutorialAdmin(admin.ModelAdmin):
	'''
	Shows the Tutorial fields in the default Django admin
	'''
	list_display = ["tutorial_date", "tutorial_start_time", "tutorial_end_time", "tutorial_group", "tutorial_location"]

# Actually registers the above with the Django admin
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Tutorial, TutorialAdmin)