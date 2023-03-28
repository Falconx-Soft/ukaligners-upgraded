from django.contrib import admin
from .models import Clinic
# Register your models here.

class Clinic_admin(admin.ModelAdmin):
	list_display = ['user','building_number','street','town','postcode','country','number']
	class Meta:
		model = Clinic

admin.site.register(Clinic,Clinic_admin)