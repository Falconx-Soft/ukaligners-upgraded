from django.contrib import admin
from .models import Technician
# Register your models here.

class Technician_admin(admin.ModelAdmin):
	list_display = ['user','number','fee','outstanding']
	class Meta:
		model = Technician

admin.site.register(Technician,Technician_admin)