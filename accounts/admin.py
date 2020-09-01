from django.contrib import admin
from .models import Manager, Profile
# Register your models here.


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user','category']

admin.site.register(Manager,ManagerAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','profile_picture','category','bio']

admin.site.register(Profile, ProfileAdmin)