from django.contrib import admin
from .models import *
# Register your models here.

class Dentist_admin(admin.ModelAdmin):
	list_display = ['user','surname','number','manager','code']
	class Meta:
		model = Dentist

admin.site.register(Dentist,Dentist_admin)


class Clinic_admin(admin.ModelAdmin):
	list_display = ['name','building_number','street','town','postcode','country','number','email']
	class Meta:
		model = Clinic

admin.site.register(Clinic,Clinic_admin)