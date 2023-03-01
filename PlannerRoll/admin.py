from django.contrib import admin
from .models import Planner
# Register your models here.

class Planner_admin(admin.ModelAdmin):
	list_display = ['user','number','fee','outstanding']
	class Meta:
		model = Planner

admin.site.register(Planner,Planner_admin)