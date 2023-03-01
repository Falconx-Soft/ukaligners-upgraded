from django.contrib import admin
from .models import *
# Register your models here.

class Manager_admin(admin.ModelAdmin):
	list_display = ['user','number','fee','outstanding']
	class Meta:
		model = Manager

admin.site.register(Manager,Manager_admin)